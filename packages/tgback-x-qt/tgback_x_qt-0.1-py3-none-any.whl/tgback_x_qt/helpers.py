import sys

from os import getenv
from io import StringIO

from asyncio import set_event_loop
from code import InteractiveConsole
from inspect import iscoroutinefunction
from platform import uname as platform_uname

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from tgback_x.version import VERSION as X_VERSION

from PySide6.QtCore import (
    Qt, QSize, Signal, Slot, QObject,
    QRunnable, QRect, QEvent, QEasingCurve,
    QPropertyAnimation
)
from PySide6.QtGui import (
    QMovie, QPixmap, QPainter, QBrush,
    QFontDatabase, QFont
)
from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QPlainTextEdit,
    QStackedWidget, QGraphicsOpacityEffect
)
from .version import VERSION
from .defaults import API_ID, API_HASH

# Take values from env variables, if present
API_ID = getenv('TGBX_API_ID') or API_ID
API_HASH = getenv('TGBX_API_HASH') or API_HASH


class CustomSignals(QObject):
    """
    With this class you can create custom object to
    emit signals from. For example:
    ...
    cs = CustomSignals(finished=bool, result=object, error=tuple)
    cs.finished.connect(self.finished)
    ...
    """
    def __init__(self, **kwargs):
        super().__init__()

        signal_class_attrs = {
            name: Signal(signal_type) for name,
            signal_type in kwargs.items()
        }
        self._signals = type("_", (QObject,), signal_class_attrs)()

    def __getattr__(self, name):
        return getattr(self._signals, name)

class Worker(QRunnable):
    """
    Class helper for running functions in separate Thread.

    "fn" is target function, "args" and "kwarg"s are,
    obviously, arguments and keyword arguments to it.

    If you need to run some async-bound function
    use .set_event_loop(loop), otherwise you will
    get RuntimeError, as Dummy thread will be
    created without any event loops.
    """
    def __init__(self, fn, *args, **kwargs):
        super().__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.loop = None

        self.signals = CustomSignals(
            result=object,
            error=Exception,
            finished=None)

    def set_event_loop(self, loop):
        """Use this if you need to run async-bound coro/func"""
        self.loop = loop

    def run(self):
        try:
            if self.loop:
                set_event_loop(self.loop)

            if iscoroutinefunction(self.fn):
                result = self.loop.run_until_complete(
                    self.fn(*self.args, **self.kwargs))
            else:
                result = self.fn(*self.args, **self.kwargs)

        except Exception as e:
            self.signals.error.emit(e)
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()

class AnimatedStackedWidget(QStackedWidget):
    def __init__(self, animation_duration=200):
        super().__init__()
        self.animation_duration = animation_duration # Animation duration (msec)
        self._animation_running = False # Prevent overlapping animations
        self._fade_out_animation = None # Store fade-out animation
        self._fade_in_animation = None # Store fade-in animation
        self._current_opacity_effect = None  # Store opacity effects
        self._next_opacity_effect = None

    def setCurrentIndex(self, index):
        if self._animation_running or self.currentIndex() == index:
            return # Ignore if an animation is already running or no change

        self._animation_running = True

        current_widget = self.currentWidget()
        next_widget = self.widget(index)

        if not current_widget or not next_widget:
            super(AnimatedStackedWidget, self).setCurrentIndex(index)
            self._animation_running = False
            return

        # Apply opacity effects to widgets
        self._current_opacity_effect = QGraphicsOpacityEffect()
        current_widget.setGraphicsEffect(self._current_opacity_effect)

        self._next_opacity_effect = QGraphicsOpacityEffect()
        next_widget.setGraphicsEffect(self._next_opacity_effect)

        # Initially hide the next widget
        self._next_opacity_effect.setOpacity(0)
        next_widget.show()

        # Create fade-out animation for the current widget
        self._fade_out_animation = QPropertyAnimation(
            self._current_opacity_effect, b'opacity')
        self._fade_out_animation.setDuration(self.animation_duration)
        self._fade_out_animation.setStartValue(1.0)
        self._fade_out_animation.setEndValue(0.0)
        self._fade_out_animation.setEasingCurve(QEasingCurve.InOutQuad)

        # Create fade-in animation for the next widget
        self._fade_in_animation = QPropertyAnimation(
            self._next_opacity_effect, b'opacity')
        self._fade_in_animation.setDuration(self.animation_duration)
        self._fade_in_animation.setStartValue(0.0)
        self._fade_in_animation.setEndValue(1.0)
        self._fade_in_animation.setEasingCurve(QEasingCurve.InOutQuad)

        def on_fade_out_finished():
            """Callback after fade-out is finished."""
            super(AnimatedStackedWidget, self).setCurrentIndex(index)
            self._fade_in_animation.start() # Start the fade-in animation

        def on_fade_in_finished():
            """Callback after fade-in is finished."""
            current_widget.setGraphicsEffect(None) # Reset effects and flags
            next_widget.setGraphicsEffect(None)
            self._animation_running = False

        self._fade_out_animation.finished.connect(on_fade_out_finished)
        self._fade_in_animation.finished.connect(on_fade_in_finished)
        self._fade_out_animation.start()

class ProgressOverlay(QWidget):
    """
    This is a fairly simple Widget that will show progress
    animataion and block all input while on top.
    """
    def __init__(self, parent: QWidget, spinner_gif: str):
        super().__init__(parent)
        self.setGeometry(parent.rect())

        self.spinner_gif = spinner_gif

        self.spinner_label = QLabel(self)
        self.spinner_label.setAlignment(Qt.AlignCenter)
        self.spinner_label.setFixedSize(QSize(80, 80))

        self.spinner_movie = QMovie(self.spinner_gif)
        self.spinner_movie.setScaledSize(self.spinner_label.size())
        self.spinner_label.setMovie(self.spinner_movie)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.spinner_label, alignment=Qt.AlignCenter)

    def show_spinner(self):
        """Show spinner circle"""
        self.parent().setEnabled(False)
        self.spinner_movie.start()
        self.setFocus()
        self.spinner_movie.start()
        self.show()

    def hide_spinner(self):
        """Hide spinner circle"""
        self.parent().setEnabled(True)
        self.spinner_movie.stop()
        self.hide()

class PythonConsole(QWidget):
    """
    This Widget implements Interactive Python Console, similar
    to default Python's IE (though much simpler).
    """
    def __init__(self, app_globals=None):
        super().__init__()
        self.setWindowTitle("TGBACK-XQt Console")
        self.setGeometry(0, 0, 666, 666)

        self.setStyleSheet('''
            QWidget { background: #060606; }

            QPlainTextEdit {
                border: 2px solid white;
            }'''
        )
        layout = QVBoxLayout(self)
        self.console_output = QPlainTextEdit(self)
        self.console_output.setReadOnly(True)

        start_message = (
            '!! WARNING !! NEVER PASTE HERE CODE YOU DON\'T TRUST !!\n\n'
            '# Welcome to the Interactive Python Console!\n'
            '# You can access TelegramClient object from "client"\n'
        )
        self.console_output.appendPlainText(start_message)

        self.console_input = QPlainTextEdit(self)
        self.console_input.setFixedHeight(150)
        self.console_input.installEventFilter(self)

        self.console_input.setPlainText('print(client.get_me()) # Type your code here')
        try:
            font_id = QFontDatabase.addApplicationFont(":/fonts/roboto_mono.ttf")
            font = QFont(QFontDatabase.applicationFontFamilies(font_id)[0])

            self.console_input.setFont(font)
            self.console_output.setFont(font)
        except IndexError:
            print('Unable to load font in PythonConsole!!!')

        layout.addWidget(self.console_output)
        layout.addWidget(self.console_input)

        self.interpreter = InteractiveConsole(app_globals or {})
        self.multi_line_buffer = ''

    def eventFilter(self, source, event):
        """Capture Enter key presses in the input field."""
        if source is self.console_input and event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                if event.modifiers() == Qt.ShiftModifier:
                    return False
                self.execute_code()
                return True

            if event.key() == Qt.Key_Tab:
                # Replace Tab with 4 spaces
                cursor = self.console_input.textCursor()
                cursor.insertText('    ')  # Insert 4 spaces
                return True
        return super().eventFilter(source, event)

    def execute_code(self):
        """Executes code from the input area."""
        code = self.console_input.toPlainText()
        self.console_input.clear()

        self.console_output.appendPlainText(f'>>> {code}')

        # Handle multiple lines by buffering input
        self.multi_line_buffer += '\n' + code
        result = self.run_interpreter_code(self.multi_line_buffer)

        # If code is complete (no syntax errors), reset buffer
        if result is not None:
            self.multi_line_buffer = ''

        if result:
            self.console_output.appendPlainText(result)

    def run_interpreter_code(self, code):
        """Run code in the interactive console and capture output."""
        old_excepthook = sys.excepthook
        sys.excepthook = sys.__excepthook__

        old_stdout = sys.stdout
        old_stderr = sys.stderr

        sys.stdout = StringIO()
        sys.stderr = StringIO()
        try:
            self.interpreter.push(code)
            output = sys.stdout.getvalue() + sys.stderr.getvalue()
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            sys.excepthook = old_excepthook

        return output

class SimpleTextWidget(QWidget):
    """
    Yes. This is Simple text Widget. Yes, you need to connect
    to 'update_log' slot and push your data. Yes, you can
    set 'clear' to False to append instead of re-write.
    """
    def __init__(self, title: str, text: str=None,
            read_only: bool=True, clear: bool=True):

        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, 666, 666)

        self.setStyleSheet('''
            QWidget { background: #060606; }

            QPlainTextEdit {
                border: 2px solid white;
            }'''
        )
        layout = QVBoxLayout(self)

        self.log = QPlainTextEdit(self)
        self.log.setReadOnly(read_only)
        self.log.setPlainText(text or '')

        try:
            font_id = QFontDatabase.addApplicationFont(":/fonts/roboto_mono.ttf")
            font = QFont(QFontDatabase.applicationFontFamilies(font_id)[0])
            self.log.setFont(font)
        except IndexError:
            print('Unable to load font in SimpleTextWidget!!!')

        layout.addWidget(self.log)
        self.setLayout(layout)

        # If clear is True we will clear
        # old text before writing new.
        self._clear = clear

    @Slot()
    def update_log(self, text: str):
        """Set the text in the read-only QPlainTextEdit."""
        if self._clear:
            self.log.setPlainText('')
        self.log.setPlainText(text)

def get_telegram_client(session: str=None) -> TelegramClient:
    """Will return TelegramClient object (without connection)"""
    u = platform_uname()

    return TelegramClient(
        session=StringSession(session),
        api_id=API_ID,
        api_hash=API_HASH,
        app_version=f'{VERSION}_{X_VERSION}',
        device_model=f'{u.system}({u.node})',
        system_version=u.release
    )

def make_circular_pixmap(pixmap: QPixmap, size: int=None) -> QPixmap:
    """
    This function will convert a square QPixmap into
    the round-corners QPixmap and return.
    """
    if size:
        pixmap = pixmap.scaled(size, size,
            Qt.KeepAspectRatio, Qt.SmoothTransformation)

    size = min(pixmap.width(), pixmap.height())
    circular_pixmap = QPixmap(size, size)
    circular_pixmap.fill(Qt.transparent)

    painter = QPainter(circular_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setBrush(QBrush(pixmap))
    painter.setPen(Qt.NoPen)
    painter.drawEllipse(QRect(0, 0, size, size))
    painter.end()

    return circular_pixmap

def int_to_bytes(int_: int, length: int=None, signed: bool=False) -> bytes:
    """Converts int to bytes with Big byteorder."""

    bit_length = int_.bit_length()

    if not length:
        if signed and not (int_ >= -128 and int_ <= 127):
            divide_with = 16
        else:
            divide_with = 8

        bit_length = ((bit_length + divide_with) // divide_with)
        length = (bit_length * divide_with) // 8

    return int.to_bytes(int_, length, 'big', signed=signed)
