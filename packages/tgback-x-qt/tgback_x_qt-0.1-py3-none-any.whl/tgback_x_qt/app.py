import sys
import traceback

from os import getenv
from io import BytesIO

from pathlib import Path
from datetime import date
from hashlib import sha256

from re import search as re_search
from math import log2 as math_log2

from random import Random
from time import time, sleep
from asyncio import new_event_loop, set_event_loop

from PySide6.QtWidgets import (
    QApplication, QStackedWidget, QWidget, QLineEdit,
    QMessageBox, QPushButton, QComboBox
)
from PySide6.QtGui import (
    QFontDatabase, QDesktopServices,
    QRegularExpressionValidator, QPixmap,
    QIcon, QCursor
)
from PySide6.QtCore import (
    Qt, QRegularExpression, Slot, Signal, QThreadPool,
    QEvent, QTimer, QFile
)
from PySide6.QtUiTools import QUiLoader

from .helpers import (
    ProgressOverlay, Worker, make_circular_pixmap,
    int_to_bytes, PythonConsole, get_telegram_client,
    AnimatedStackedWidget, SimpleTextWidget
)
from .defaults import BIRTHDAY_FORMAT, TELEGRAM_USERBOT_PHONE
from .version import VERSION

from darkdetect import isDark as darkdetect_isDark
from phrasegen import Generator as phrasegen_Generator

from telethon.errors import (
    PhoneNumberBannedError, PhoneNumberFloodError,
    PhoneNumberInvalidError, SessionPasswordNeededError,
    PhoneCodeInvalidError, PasswordHashInvalidError,
    SendCodeUnavailableError
)
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest

from tgback_x.defaults import Scrypt
from tgback_x.errors import Tgback_X_Error
from tgback_x.providers import PROVIDER_MAP
from tgback_x.crypto import make_scrypt_key, Key
from tgback_x.version import VERSION as X_VERSION

LOOP = new_event_loop()
set_event_loop(LOOP)

if getattr(sys, 'frozen', False): # Check if running as .EXE
    ABSPATH = Path(sys._MEIPASS)
else:
    ABSPATH = Path(__file__).parent.absolute()

UIPATH  = ABSPATH / 'ui'
RESPATH = ABSPATH / 'resources'
STYPATH = ABSPATH / 'stylesheet'

DARK_STYLE = open(STYPATH / 'dark.qss', encoding='utf-8').read()
BRIGHT_STYLE = open(STYPATH / 'bright.qss', encoding='utf-8').read()

# If None decide automatically, Dark if "1", Bright otherwise.
DARK_MODE = getenv('TGBX_DARK_MODE')
# PySide6 style, e.g Windows10 or Fusion. Fusion if None.
APP_STYLE = getenv('TGBX_APP_STYLE')
# Will launch Console on app start if present
LAUNCH_CONSOLE = getenv('TGBX_LAUNCH_CONSOLE')

# The TGBX_API_ID & TGBX_API_HASH env vars are
# in helpers.py file.

try:
    from .resources._build import img_rc # pylint: disable=W0611
    from .resources._build import fonts_rc # pylint: disable=W0611
except ModuleNotFoundError as e:
    raise RuntimeError('You need to build Resources firstly!') from e

class StartScreen(QWidget):
    switch_widget: Signal = Signal(int)
    change_theme: Signal = Signal(str)
    provider: Signal = Signal(str)

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self.ui.make_backup.clicked.connect(self.make_backup_clicked)
        self.ui.open_backup.clicked.connect(self.open_backup_clicked)
        self.ui.change_theme.clicked.connect(self.change_theme_clicked)
        self.ui.github_button.clicked.connect(self.github_button_clicked)
        self.ui.about_button.clicked.connect(self.about_button_clicked)

        for k in PROVIDER_MAP.keys():
            if k != 'TelegramChannel': # default one
                self.ui.provider_select.addItem(k)

    @Slot()
    def about_button_clicked(self):
        about = (
         f'<b>TGBACK-XQt v{VERSION} (tgback-x v{X_VERSION})</b><br><br>'

          '→ <a href="https://github.com/NonProjects/tgback-x"><b>TGBACK-X</b></a> '
          '(& <a href="https://github.com/NotStatilko/tgback-x-qt"><b>Qt App</b></a>) '
          'is made by <a href="https://github.com/NotStatilko/"><b>NotStatilko</b>'

          '</a>.<br>→ Cool <b>cloud Icon</b> is designed & made by <a href="'
          'https://flaticon.com/authors/pocike"><b>Pocike</b></a>.<br><br>'

          '(the <a href="https://en.wikipedia.org/wiki/MIT_License"><b>'
          'MIT License</b></a>)'
        )
        display_popup(about, type_='Information', title='About', rich=True)

    @Slot()
    def make_backup_clicked(self):
        self.provider.emit(self.ui.provider_select.currentText())
        self.switch_widget.emit(2)

    @Slot()
    def open_backup_clicked(self):
        self.provider.emit(self.ui.provider_select.currentText())
        self.switch_widget.emit(6)

    @Slot()
    def change_theme_clicked(self):
        if QApplication.instance().styleSheet() == DARK_STYLE:
            cs = BRIGHT_STYLE
        else:
            cs = DARK_STYLE

        self.change_theme.emit(cs)

    @Slot()
    def github_button_clicked(self):
        QDesktopServices.openUrl('https://github.com/NotStatilko/tgback-x-qt')


class CreatePhrase(QWidget):
    switch_widget: Signal = Signal(int)
    keydata_phrase: Signal = Signal(str)

    change_scrypt_switch: Signal = Signal(int)
    change_birthday_switch: Signal = Signal(int)

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self.generator = phrasegen_Generator()

        self._stage = 0 # Stage means where are we now
        self._last_choice = None # 0 would be Random phrase, 1 is User password

        self.ui.phrase_input.hide()
        self.ui.phrase_widget.hide()
        self.ui.tips_text.hide()
        self.ui.continue_button.hide()
        self.ui.hide_pass_widget.hide()
        self.ui.show_pass_widget.hide()
        self.ui.setup_scrypt_button.hide()

        self.ui.lang_select.hide()
        self.ui.lang_select.addItem('en')

        for code in sorted(self.generator.supported_languages):
            if code != 'en':
                self.ui.lang_select.addItem(code)

        self.ui.lang_select.currentIndexChanged.connect(self.lang_select_changed)

        self.ui.move_back.clicked.connect(self.move_back_clicked)
        self.ui.gen_phrase.clicked.connect(self.gen_phrase_clicked)
        self.ui.use_phrase.clicked.connect(self.use_phrase_clicked)
        self.ui.continue_button.clicked.connect(self.continue_button_clicked)
        self.ui.show_password.clicked.connect(self.show_password_clicked)
        self.ui.hide_password.clicked.connect(self.hide_password_clicked)
        self.ui.setup_scrypt_button.clicked.connect(self.setup_scrypt_clicked)

        self.ui.custom_phrase.returnPressed.connect(self.continue_button_clicked)
        self.ui.r_custom_phrase.returnPressed.connect(self.continue_button_clicked)

    @Slot()
    def reset_ui(self):
        # Reset UI. Typically this is signal from Account
        # Move Back button.
        self._stage = 0

        self.ui.phrase_input.hide()
        self.ui.phrase_widget.hide()
        self.ui.tips_text.hide()
        self.ui.continue_button.hide()
        self.ui.hide_pass_widget.hide()
        self.ui.show_pass_widget.hide()
        self.ui.setup_scrypt_button.hide()
        self.ui.lang_select.hide()

        self.ui.phrase_select.show()

    @Slot()
    def move_back_clicked(self):
        if self._stage == 0:
            self.switch_widget.emit(0)

        elif self._stage == 1:
            self.ui.phrase_widget.hide()
            self.ui.phrase_input.hide()
            self.ui.tips_text.hide()
            self.ui.continue_button.hide()
            self.ui.hide_pass_widget.hide()
            self.ui.show_pass_widget.hide()
            self.ui.lang_select.hide()
            self.ui.setup_scrypt_button.hide()

            self.ui.phrase_select.show()

        if self._stage > 0:
            self._stage -= 1

    @Slot()
    def gen_phrase_clicked(self):
        self._stage = 1
        self._last_choice = 0

        display_popup(
            'Please note that ANY user of TGBACK-X that will be able to type '
            'your Passphrase will OBTAIN A FULL ACCESS TO YOUR BACKUP '
            'DATA, which includes a FULL ACCESS TO YOUR TELEGRAM ACCOUNT. '
            'Before proceeding and connecting your account, MAKE SURE that '
            'your computer has NO malware and you TRUST it, e.g nobody can track '
            'your keystrokes & nobody can capture your screen.\n\nA good bonus '
            'recommendation would be to ALWAYS store Passphrase on paper only. '
            'Treat it as a Bitcoin seed phrase, if that make sense to You.',

            type_='Warning'
        )
        self.ui.phrase_select.hide()
        self.lang_select_changed()
        self.ui.phrase_widget.show()
        self.ui.tips_text.show()
        self.ui.continue_button.show()
        self.ui.lang_select.show()
        self.ui.setup_scrypt_button.show()

    @Slot()
    def use_phrase_clicked(self):
        self._stage = 1
        self._last_choice = 1

        display_popup(
            'Please note that ANY user of TGBACK-X that will be able to type '
            'your custom Password will OBTAIN A FULL ACCESS TO YOUR BACKUP '
            'DATA, which includes a FULL ACCESS TO YOUR TELEGRAM ACCOUNT. '
            'Before proceeding and connecting your account, MAKE SURE that '
            'your computer has NO malware and you TRUST it, nobody can track '
            'your keystrokes & nobody can capture your screen.\n\nThis option '
            'is ONLY for experienced users who utilize password generators! '
            'NEVER use your own passwords here, as they are most probably not '
            'secure. Go back and use Recommended by App option instead.',

            type_='Warning'
        )
        self.ui.phrase_select.hide()
        self.ui.phrase_input.show()
        self.ui.show_pass_widget.show()
        self.ui.continue_button.show()
        self.ui.setup_scrypt_button.show()

    @Slot()
    def continue_button_clicked(self):
        if self._last_choice == 0: # App generated Phrase
            self.keydata_phrase.emit(self.ui.phrase.toPlainText())
        else: # User-specified password
            conditions = (
                self.ui.custom_phrase.text() == self.ui.r_custom_phrase.text(),
                bool(self.ui.custom_phrase.text()),
                bool(self.ui.r_custom_phrase.text())
            )
            if not all(conditions):
                for linedit in (self.ui.custom_phrase, self.ui.r_custom_phrase):
                    linedit.setStyleSheet(
                        'QLineEdit {border: 2px solid #d22f00;}\n'
                        'QLineEdit:focus {border: 2px solid #808080;}'
                    )
                return

            for linedit in (self.ui.custom_phrase, self.ui.r_custom_phrase):
                linedit.setStyleSheet('')

            self.ui.hide_pass_widget.hide()
            self.ui.show_pass_widget.show()

            self.ui.custom_phrase.setEchoMode(QLineEdit.Password)
            self.ui.r_custom_phrase.setEchoMode(QLineEdit.Password)
            self.keydata_phrase.emit(self.ui.custom_phrase.text())

        self.change_birthday_switch.emit(0)
        self.switch_widget.emit(3)

    @Slot()
    def show_password_clicked(self):
        self.ui.show_pass_widget.hide()
        self.ui.hide_pass_widget.show()
        self.ui.custom_phrase.setEchoMode(QLineEdit.Normal)
        self.ui.r_custom_phrase.setEchoMode(QLineEdit.Normal)

    @Slot()
    def hide_password_clicked(self):
        self.ui.hide_pass_widget.hide()
        self.ui.show_pass_widget.show()
        self.ui.custom_phrase.setEchoMode(QLineEdit.Password)
        self.ui.r_custom_phrase.setEchoMode(QLineEdit.Password)

    @Slot()
    def setup_scrypt_clicked(self):
        self.change_scrypt_switch.emit(0)
        self.switch_widget.emit(4)

    @Slot()
    def lang_select_changed(self):
        code = self.ui.lang_select.currentText()
        lang_gen = getattr(self.generator, code)
        phrase = lang_gen.generate(8)
        self.ui.phrase.setPlainText(phrase)


class InputBirthday(QWidget):
    switch_widget: Signal = Signal(int)
    keydata_birthd: Signal = Signal(str)
    open_backup_in_account: Signal = Signal()

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self._switch_state = 0 # We will emit signal to hint this class to which
                              # class to switch when "move" button is clicked,
                              # where 0 means that we're in CreateBackup state
                              # and 1 that we're in OpenBackup state.
        regexp = QRegularExpression(r'^(0?[1-9]|[12][0-9]|3[01])$')
        validator = QRegularExpressionValidator(regexp, self)
        self.ui.day.setValidator(validator)

        regexp = QRegularExpression(r'^(0?[1-9]|1[0-2])$')
        validator = QRegularExpressionValidator(regexp, self)
        self.ui.month.setValidator(validator)

        regexp = QRegularExpression(r'^\d{4}$')
        validator = QRegularExpressionValidator(regexp, self)
        self.ui.year.setValidator(validator)

        self.ui.why_ask_button.clicked.connect(self.why_ask_button_clicked)
        self.ui.continue_button.clicked.connect(self.continue_button_clicked)
        self.ui.move_back.clicked.connect(self.move_back_clicked)

        self.ui.day.returnPressed.connect(self.continue_button_clicked)
        self.ui.month.returnPressed.connect(self.continue_button_clicked)
        self.ui.year.returnPressed.connect(self.continue_button_clicked)

    @Slot()
    def why_ask_button_clicked(self):
        display_popup(
           'This data will be mixed to encryption Key to enhance it\'s '
            'strength. Your birthday is never shared with anyone.',
            type_='Information')

    @Slot()
    def continue_button_clicked(self):
        inputs_incorrect = False
        for input_ in (self.ui.day, self.ui.month, self.ui.year):
            if not input_.text() or int(input_.text()) < 1 or\
                (input_ is self.ui.year and len(input_.text()) < 4):
                    input_.setStyleSheet(
                        'QLineEdit {border: 2px solid #d22f00;}\n'
                        'QLineEdit:focus {border: 2px solid #808080;}'
                    )
                    inputs_incorrect = True
            else:
                input_.setStyleSheet('')

        if inputs_incorrect:
            return

        birthday = date(
            year=int(self.ui.year.text()),
            month=int(self.ui.month.text()),
            day=int(self.ui.day.text())
        )
        self.keydata_birthd.emit(birthday.strftime(BIRTHDAY_FORMAT))

        if self._switch_state == 0: # We're creating backup
            self.switch_widget.emit(1)
        else: # We're opening backup
            self.open_backup_in_account.emit()
            self.switch_widget.emit(5)

    @Slot()
    def change_switch_state(self, switch_state: int):
        self._switch_state = switch_state

    @Slot()
    def move_back_clicked(self):
        self.switch_widget.emit(2 if self._switch_state == 0 else 6)

    @Slot()
    def switch_to_account(self, result):
        self.tg_session.emit(result.session.save())
        self.switch_widget.emit(5)


class SetupScrypt(QWidget):
    switch_widget: Signal = Signal(int)

    scrypt_n: Signal = Signal(int)
    scrypt_r: Signal = Signal(int)
    scrypt_p: Signal = Signal(int)
    scrypt_dklen: Signal = Signal(int)
    scrypt_salt: Signal = Signal(str)

    lock_phrase_interface: Signal = Signal()

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self._switch_state = 0 # We will emit signal to hint this class to which
                              # class to switch when "move" button is clicked,
                              # where 0 means that we're in CreateBackup state
                              # and 1 that we're in OpenBackup state.
        self.ui.scrypt_N.setText(str(Scrypt.N))
        self.ui.scrypt_R.setText(str(Scrypt.R))
        self.ui.scrypt_P.setText(str(Scrypt.P))
        self.ui.scrypt_Dklen.setText(str(Scrypt.DKLEN))
        self.ui.scrypt_Salt.setText(hex(Scrypt.SALT)[2:].upper())

        self.ui.move_back.clicked.connect(self.move_back_clicked)
        self.ui.help_scrypt.clicked.connect(self.help_scrypt_clicked)

        regexp = QRegularExpression(r'^[1-9]\d*$')
        validator = QRegularExpressionValidator(regexp, self)

        self.ui.scrypt_N.setValidator(validator)
        self.ui.scrypt_R.setValidator(validator)
        self.ui.scrypt_P.setValidator(validator)
        self.ui.scrypt_Dklen.setValidator(validator)

        regexp = QRegularExpression(r'^[0-9A-Fa-f]+$')
        validator = QRegularExpressionValidator(regexp, self)
        self.ui.scrypt_Salt.setValidator(validator)

    @Slot()
    def move_back_clicked(self):
        linedits = (
            self.ui.scrypt_N, self.ui.scrypt_R, self.ui.scrypt_P,
            self.ui.scrypt_Dklen, self.ui.scrypt_Salt
        )
        for linedit in linedits:
            if not linedit.text():
                linedit.setStyleSheet(
                    'QLineEdit {border: 2px solid #d22f00;}\n'
                    'QLineEdit:focus {border: 2px solid #808080;}'
                )
                return

        # N must be pow of 2 and > 0
        n_log2 = math_log2(int(self.ui.scrypt_N.text()))

        if n_log2 == 0 or not n_log2.is_integer():
            self.ui.scrypt_N.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return

        self.ui.scrypt_N.setStyleSheet('')

        if len(self.ui.scrypt_Salt.text()) % 2:
            self.ui.scrypt_Salt.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return
        try:
            bytes.fromhex(self.ui.scrypt_Salt.text())
        except:
            self.ui.scrypt_Salt.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return

        for linedit in linedits:
            linedit.setStyleSheet('')

        self.scrypt_n.emit(int(self.ui.scrypt_N.text()))
        self.scrypt_r.emit(int(self.ui.scrypt_R.text()))
        self.scrypt_p.emit(int(self.ui.scrypt_P.text()))
        self.scrypt_dklen.emit(int(self.ui.scrypt_Dklen.text()))
        self.scrypt_salt.emit(self.ui.scrypt_Salt.text())

        if self._switch_state == 0: # Zero is Create Phrase
            self.lock_phrase_interface.emit()

        self.switch_widget.emit(2 if self._switch_state == 0 else 6)

    @Slot()
    def help_scrypt_clicked(self):
        display_popup(
            'If You don\'t know what Scrypt is then you probably '
            'should NOT touch anything here. This is a safe '
            'defaults.<br><br>Check out article on '
            '<a href="https://en.wikipedia.org/wiki/'
            'Scrypt"><b>Wikipedia</b></a> about Scrypt KDF.',

            type_='Information',
            rich=True
        )

    @Slot()
    def change_switch_state(self, switch_state: int):
        self._switch_state = switch_state


class CreateBackup(QWidget):
    switch_widget: Signal = Signal(int)
    tg_session: Signal = Signal(str)

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self.ui.move_back.clicked.connect(self.move_back_clicked)
        self.ui.request_code.clicked.connect(self.request_code_clicked)
        self.ui.check_code.clicked.connect(self.check_code_clicked)
        self.ui.show_password.clicked.connect(self.show_password_clicked)
        self.ui.hide_password.clicked.connect(self.hide_password_clicked)
        self.ui.sign_in.clicked.connect(self.sign_in_clicked)

        self._stage = 0 # Stage means where are we now. Firstly, user needs
                        # to input phone number, then code, then pass. For
                        # each of this stages we will increment this and check
        self.ui.login_code_widget.hide()
        self.ui.password_widget.hide()

        self.ui.hide_pass_widget.hide()
        self.ui.show_pass_widget.hide()

        self.ui.phone_number.returnPressed.connect(self.request_code_clicked)
        self.ui.login_code.returnPressed.connect(self.check_code_clicked)
        self.ui.password.returnPressed.connect(self.sign_in_clicked)

        regexp = QRegularExpression(r'^\d{0,15}$')
        validator = QRegularExpressionValidator(regexp, self)
        self.ui.phone_number.setValidator(validator)

        regexp = QRegularExpression(r'^\d{0,6}$')
        validator = QRegularExpressionValidator(regexp, self)
        self.ui.login_code.setValidator(validator)

        self.progress_overlay = ProgressOverlay(
            self, spinner_gif=':/images/img/loading_spinner.gif')
        self.progress_overlay.hide()

        self.tpool = QThreadPool()

        self._tc = None
        self._phone_number = None
        self._login_code = None
        self._password = None

    def event(self, event): # Reloading default event()
        if event.type() == QEvent.Show:
            self._connect_tc()
        return super().event(event)

    def _connect_tc(self):
        if self._tc is None:
            self._tc = get_telegram_client()

        if not self._tc.is_connected():
            worker = Worker(self._tc.connect)
            worker.set_event_loop(LOOP)

            worker.signals.finished.connect(self.hide_progress_overlay)
            worker.signals.error.connect(self.worker_error)

            self.progress_overlay.show_spinner()
            self.tpool.start(worker)

    @Slot()
    def reset_ui(self):
        # Reset UI. Typically this is signal from Account
        # Move Back button.
        self._stage = 0
        self.ui.login_code_widget.hide()
        self.ui.password_widget.hide()
        self.ui.hide_pass_widget.hide()
        self.ui.show_pass_widget.hide()
        self.ui.request_code_widget.show()

        self._tc = get_telegram_client()

    @Slot()
    def move_back_clicked(self):
        if self._stage == 0:
            try:
                if self._tc.is_connected():
                    self._tc.disconnect()
            except:
                pass # Doesn't really matter much

            self._tc = None
            self.switch_widget.emit(3)

        elif self._stage == 1:
            self.ui.login_code_widget.hide()
            self.ui.request_code_widget.show()

        elif self._stage == 2:
            self.ui.password_widget.hide()
            self.ui.login_code_widget.show()

            self.ui.password.setEchoMode(QLineEdit.Password)
            self.ui.show_pass_widget.hide()
            self.ui.hide_pass_widget.hide()

        if self._stage > 0:
            self._stage -= 1

    @Slot()
    def request_code_clicked(self):
        error_raised = True
        try:
            assert self.ui.phone_number.text()
            self._tc.send_code_request(self.ui.phone_number.text())
        except PhoneNumberBannedError as e:
            display_popup('This phone number was banned by Telegram!', e)
        except PhoneNumberFloodError as e:
            display_popup('Too many requests! Try again later.', e)
        except PhoneNumberInvalidError as e:
            display_popup('Invalid phone number. Check your input.', e)
        except SendCodeUnavailableError as e:
            display_popup('Telegram already sent you code.', e, type_='Information')
            error_raised = False # This is not an error, rather Warning here.
        except AssertionError:
            pass
        else:
            error_raised = False

        if error_raised:
            self.ui.phone_number.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return

        self.ui.phone_number.setStyleSheet('')
        self._stage = 1

        self.ui.request_code_widget.hide()
        self.ui.login_code_widget.show()

    @Slot()
    def check_code_clicked(self):
        error_raised = True
        try:
            assert not len(self.ui.login_code.text()) < 5
            self._tc.sign_in(self.ui.phone_number.text(), self.ui.login_code.text())
        except AssertionError:
            pass
        except PhoneCodeInvalidError as e:
            display_popup('Invalid code. Check your input.', e)

        except SessionPasswordNeededError:
            self.ui.login_code_widget.hide()
            self.ui.password_widget.show()
            self.ui.show_pass_widget.show()

            self._stage = 2
            error_raised = False
        else:
            error_raised = False
            self.tg_session.emit(self._tc.session.save())
            self.switch_widget.emit(5)

        if error_raised:
            self.ui.login_code.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return

        self.ui.login_code.setStyleSheet('')

    @Slot()
    def sign_in_clicked(self):
        error_raised = True
        try:
            self._tc.sign_in(password=self.ui.password.text())
        except PasswordHashInvalidError as e:
            display_popup('Incorrect password. Check your input.', e)
        else:
            self._stage = 0
            error_raised = False
            self.ui.login_code.setText('')
            self.tg_session.emit(self._tc.session.save())
            self.switch_widget.emit(5)

        if error_raised:
            self.ui.password.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return

        self.ui.login_code.setStyleSheet('')

    @Slot()
    def show_password_clicked(self):
        self.ui.show_pass_widget.hide()
        self.ui.hide_pass_widget.show()
        self.ui.password.setEchoMode(QLineEdit.Normal)

    @Slot()
    def hide_password_clicked(self):
        self.ui.hide_pass_widget.hide()
        self.ui.show_pass_widget.show()
        self.ui.password.setEchoMode(QLineEdit.Password)

    @Slot()
    def hide_progress_overlay(self):
        self.progress_overlay.hide_spinner()

    @Slot()
    def worker_error(self, error: Exception):
        self.switch_widget.emit(3)
        display_popup('TGBACK-X refuses to perform some action. See Details.', error)


class Account(QWidget):
    switch_widget: Signal = Signal(int)
    change_birthday_switch: Signal = Signal(int)
    tg_session: Signal = Signal(str)
    reset_ui: Signal = Signal()

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self.progress_overlay = ProgressOverlay(
            self, spinner_gif=':/images/img/loading_spinner.gif')
        self.progress_overlay.hide()

        self.tpool = QThreadPool()

        self._state = 0 # If state is 0 we're making backup, if state
                        # is 1 we're opening existing one.
        self._tc = None
        self._user = None

        self._provider = None
        self._keydata_phrase = None
        self._keydata_birthd = None

        self._scrypt_n = Scrypt.N.value
        self._scrypt_r = Scrypt.R.value
        self._scrypt_p = Scrypt.P.value
        self._scrypt_dklen = Scrypt.DKLEN.value
        self._scrypt_salt = Scrypt.SALT.value

        # This would be the actual encryption key of backup
        # skey is a Scrypt (make_scrypt_key) Key.
        self._skey = None

        self.ui.profile_pic.hide()
        self.ui.name.hide()
        self.ui.username.hide()
        self.ui.scan_for_code.hide()
        self.ui.launch_terminal.hide()
        self.ui.to_start.hide()
        self.ui.my_phone.hide()
        self.ui.destroy_backup.hide()
        self.ui.are_you_sure.hide()

        self.ui.to_start.clicked.connect(self.to_start_clicked)
        self.ui.my_phone.clicked.connect(self.my_phone_clicked)
        self.ui.scan_for_code.clicked.connect(self.scan_for_code_clicked)
        self.ui.launch_terminal.clicked.connect(self.launch_terminal_clicked)
        self.ui.destroy_backup.clicked.connect(self.destroy_backup_clicked)
        self.ui.are_you_sure.clicked.connect(self.are_you_sure_clicked)

        self._console_list = []

    @Slot()
    def set_tg_client(self, tg_session: str):
        self._tc = get_telegram_client(tg_session)
        worker = Worker(self._tc.connect)
        worker.set_event_loop(LOOP)

        worker.signals.result.connect(self.show_backup)
        worker.signals.error.connect(self.worker_error)

        self.progress_overlay.show_spinner()
        self.tpool.start(worker)

    @Slot()
    def set_provider(self, provider: str):
        self._provider = provider

    @Slot()
    def set_keydata_phrase(self, keydata_phrase: str):
        self._keydata_phrase = keydata_phrase

    @Slot()
    def set_keydata_birthd(self, keydata_birthd: str):
        self._keydata_birthd = keydata_birthd

    @Slot()
    def set_scrypt_n(self, scrypt_n: int):
        self._scrypt_n = scrypt_n

    @Slot()
    def set_scrypt_r(self, scrypt_r: int):
        self._scrypt_r = scrypt_r

    @Slot()
    def set_scrypt_p(self, scrypt_p: int):
        self._scrypt_p = scrypt_p

    @Slot()
    def set_scrypt_dklen(self, scrypt_dklen: int):
        self._scrypt_dklen = scrypt_dklen

    @Slot()
    def set_scrypt_salt(self, scrypt_salt: str):
        self._scrypt_salt = int(scrypt_salt, 16)

    @Slot()
    def hide_progress_overlay(self):
        self.progress_overlay.hide_spinner()

    @Slot()
    def show_backup(self):
        if self._state == 0:
            # ------ Making TGBACK-X Backup ----------------------------------- #
            provider = PROVIDER_MAP.get(self._provider)()

            salt = int_to_bytes(self._scrypt_salt)
            salt = sha256(self._keydata_birthd.encode() + salt).digest()

            self._skey = make_scrypt_key(self._keydata_phrase.encode(),
                salt=salt, n=self._scrypt_n, r=self._scrypt_r,
                p=self._scrypt_p, dklen=self._scrypt_dklen
            )
            try:
                provider.store(Key(self._skey), self._tc)
            except Tgback_X_Error as e:
                self.reset_ui.emit()
                display_popup('Backup is impossible to create! See Details', e)
                self._tc.log_out()
                self.progress_overlay.hide_spinner()
                self.switch_widget.emit(1); return
            # ----------------------------------------------------------------- #

        self.ui.profile_pic.setToolTip(None)

        user = self._tc.get_me()
        self._user = user

        user_pic = self._tc.get_profile_photos(user.id)
        if not user_pic or user_pic[0].video_sizes:
            # I'm too lazy to implement Video profile pics :shruggy:
            pic = QPixmap(':/images/img/no_profile_pic.png')
            self.ui.profile_pic.setToolTip('Can\'t parse your profile pic. Sorry! :)')
        else:
            pic_io = BytesIO()
            self._tc.download_media(user_pic[0], file=pic_io)
            pic_io.seek(0)

            pic = QPixmap()
            pic.loadFromData(pic_io.read())

        pic = make_circular_pixmap(pic, 140)
        self.ui.profile_pic.setPixmap(pic)

        name = user.first_name + (user.last_name or '')
        self.ui.name.setText(name)

        username = f'@{user.username}' if user.username else '<no username>'
        self.ui.username.setText(username)

        self.ui.profile_pic.show()
        self.ui.name.show()
        self.ui.username.show()
        self.ui.scan_for_code.show()
        self.ui.launch_terminal.show()
        self.ui.to_start.show()
        self.ui.my_phone.show()
        self.ui.destroy_backup.show()

        self.hide_progress_overlay()

    @Slot()
    def open_backup(self):
        self._state = 1

        def open_backup(self):
            provider = PROVIDER_MAP.get(self._provider)()

            salt = int_to_bytes(self._scrypt_salt)
            salt = sha256(self._keydata_birthd.encode() + salt).digest()

            self._skey = make_scrypt_key(self._keydata_phrase.encode(),
                salt=salt, n=self._scrypt_n, r=self._scrypt_r,
                p=self._scrypt_p, dklen=self._scrypt_dklen
            )
            self._tc = provider.get(Key(self._skey))

        worker = Worker(lambda: open_backup(self))
        worker.set_event_loop(LOOP)

        worker.signals.finished.connect(self.hide_progress_overlay)
        worker.signals.result.connect(self.show_backup)
        worker.signals.error.connect(self.worker_error)

        self.progress_overlay.show_spinner()
        self.tpool.start(worker)

    @Slot()
    def worker_error(self, error: Exception):
        self.to_start_clicked()
        display_popup('Something went wrong. See Details.', error)

    @Slot()
    def backup_destroy_finished(self):
        self.to_start_clicked()
        display_popup('Backup was destroyed!', type_='Information')

    @Slot()
    def to_start_clicked(self):
        self._state = 0 # Reset state

        for console in self._console_list:
            console.hide()
        self._console_list.clear()

        self.ui.profile_pic.hide()
        self.ui.name.hide()
        self.ui.username.hide()
        self.ui.scan_for_code.hide()
        self.ui.launch_terminal.hide()
        self.ui.to_start.hide()
        self.ui.my_phone.hide()
        self.ui.are_you_sure.hide()
        self.ui.destroy_backup.hide()

        self.reset_ui.emit()
        self.switch_widget.emit(0)

    @Slot()
    def my_phone_clicked(self):
        self.ui.destroy_backup.show()
        self.ui.are_you_sure.hide()

        display_popup(f'Your phone number is {self._user.phone}',
            type_='Information')

    @Slot()
    def scan_for_code_clicked(self):
        self.tg_session.emit(self._tc.session.save()) # For Code()
        self.ui.destroy_backup.show()
        self.ui.are_you_sure.hide()
        self.switch_widget.emit(7)

    @Slot()
    def launch_terminal_clicked(self):
        globals_ = globals()
        globals_['client'] = self._tc

        console = PythonConsole(globals_)
        self._console_list.append(console)

        self.ui.destroy_backup.show()
        self.ui.are_you_sure.hide()
        console.show()

    @Slot()
    def are_you_sure_clicked(self):
        self._tc = None
        provider = PROVIDER_MAP.get(self._provider)()

        worker = Worker(lambda: provider.destroy(Key(self._skey)))
        worker.set_event_loop(LOOP)

        worker.signals.result.connect(self.backup_destroy_finished)
        worker.signals.finished.connect(self.hide_progress_overlay)
        worker.signals.error.connect(self.worker_error)

        self.progress_overlay.show_spinner()
        self.tpool.start(worker)

    @Slot()
    def destroy_backup_clicked(self):
        self.ui.destroy_backup.hide()
        self.ui.are_you_sure.show()


class OpenBackup(QWidget):
    switch_widget: Signal = Signal(int)
    keydata_phrase: Signal = Signal(str)
    change_birthday_switch: Signal = Signal(int)
    change_scrypt_switch: Signal = Signal(int)

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self.ui.hide_phrase_widget.hide()

        self.ui.hide_phrase.clicked.connect(self.hide_phrase_clicked)
        self.ui.show_phrase.clicked.connect(self.show_phrase_clicked)
        self.ui.move_back.clicked.connect(self.move_back_clicked)
        self.ui.move_forward.clicked.connect(self.move_forward_clicked)
        self.ui.setup_scrypt_button.clicked.connect(self.setup_scrypt_clicked)
        self.ui.backup_phrase.returnPressed.connect(self.move_forward_clicked)

    @Slot()
    def show_phrase_clicked(self):
        self.ui.show_phrase_widget.hide()
        self.ui.hide_phrase_widget.show()
        self.ui.backup_phrase.setEchoMode(QLineEdit.Normal)

    @Slot()
    def hide_phrase_clicked(self):
        self.ui.show_phrase_widget.show()
        self.ui.hide_phrase_widget.hide()
        self.ui.backup_phrase.setEchoMode(QLineEdit.Password)

    @Slot()
    def move_forward_clicked(self):
        if not self.ui.backup_phrase.text():
            self.ui.backup_phrase.setStyleSheet(
                'QLineEdit {border: 2px solid #d22f00;}\n'
                'QLineEdit:focus {border: 2px solid #808080;}'
            )
            return

        self.ui.backup_phrase.setStyleSheet('')

        self.ui.hide_phrase_widget.hide()
        self.ui.show_phrase_widget.show()
        self.ui.backup_phrase.setEchoMode(QLineEdit.Password)

        self.keydata_phrase.emit(self.ui.backup_phrase.text())
        self.change_birthday_switch.emit(1)
        self.switch_widget.emit(3)

    @Slot()
    def setup_scrypt_clicked(self):
        self.change_scrypt_switch.emit(1)
        self.switch_widget.emit(4)

    @Slot()
    def move_back_clicked(self):
        self.switch_widget.emit(0)


class Code(QWidget):
    switch_widget: Signal = Signal(int)
    log_update: Signal = Signal(str)

    def __init__(self, ui_file: Path):
        super().__init__()

        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)

        self.ui = QUiLoader().load(ui, self)
        ui.close()

        self._tc = None
        self._random = Random()

        # Match any 5-6 digit in string. I made 6 just in case
        # because Telegram may make login code bigger
        self._code_pattern = r'(?<!\d)\d{5,6}(?!\d)'

        self.progress_overlay = ProgressOverlay(
            self, spinner_gif=':/images/img/loading_spinner.gif')
        self.progress_overlay.hide()

        self.tpool = QThreadPool()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.randomize_label)

        self.listener = None
        self._last_code_time = None
        self._telegram_user = None
        self._me = None

        self._log = SimpleTextWidget('Telegram userbot Log')
        self.log_update.connect(self._log.update_log)

        self.ui.move_back.clicked.connect(self.move_back_clicked)
        self.ui.designer_idiot_help_me_button.clicked.connect(
            self.designer_idiot_help_me_button_clicked)
        self.ui.show_log.clicked.connect(self.show_log_clicked)

    @Slot()
    def move_back_clicked(self):
        self._tc = None
        self._log.hide()
        self.listener = None
        self.switch_widget.emit(5)

    @Slot()
    def designer_idiot_help_me_button_clicked(self):
        display_popup(
            'Here we scan chat with Telegram for login codes. Try to '
            'sign-in through your Telegram App, code should appear here.',
            type_='Information')

    @Slot()
    def show_log_clicked(self):
        if self._log.isHidden():
            self._log.show()

    @Slot()
    def set_tg_client(self, tg_session: str):
        if not self._tc:
            self._last_code_time = time()
            self._tc = get_telegram_client(tg_session)

            worker = Worker(self._tc.connect)
            worker.set_event_loop(LOOP)

            worker.signals.result.connect(self.init_listen)
            worker.signals.finished.connect(self.hide_progress_overlay)
            worker.signals.error.connect(self.worker_error)

            self.progress_overlay.show_spinner()
            self.tpool.start(worker)
        else:
            self.init_listen()

        self.start_animation()

    @Slot()
    def set_code(self, code):
        if code is not None: # None is essentialy "Stop".
            self.ui.login_code.setText(code)
            self.stop_animation()
            self.init_listen() # Continue to listen

    @Slot()
    def hide_progress_overlay(self):
        self.progress_overlay.hide_spinner()

    def start_animation(self):
        self.timer.start(500) # Mseconds

    def stop_animation(self):
        self.timer.stop()

    def randomize_label(self):
        rchar = lambda: self._random.choice('0123456789*/?')
        random_code = ''.join(rchar() for _ in range(5))
        self.ui.login_code.setText(random_code)

    @Slot()
    def init_listen(self):
        if not self._telegram_user:
            self._me = self._tc.get_me()
            try:
                self._telegram_user = self._tc.get_entity(TELEGRAM_USERBOT_PHONE)
            except ValueError: # Telegram Userbot not in Contacts
                tg_user = InputPhoneContact(
                    client_id=0,
                    phone=TELEGRAM_USERBOT_PHONE,
                    first_name='Telegram', last_name=''
                )
                request = self._tc(ImportContactsRequest([tg_user]))

                if not request.users:
                    display_popup(
                        'Could NOT import Telegram User by phone +42777. '
                        'Either Telegram changed something or App is now '
                        'outdated. Try to use Terminal.')
                    self.switch_widget.emit(5)
                    return

                self._telegram_user = request.users[0]

        self.listener = Worker(self.listen_for_code)
        self.listener.set_event_loop(LOOP)

        self.listener.signals.result.connect(self.set_code)
        self.listener.signals.error.connect(self.worker_error)

        self.tpool.start(self.listener)

    @Slot()
    def listen_for_code(self):
        while True:
            if not self._tc:
                return # May lag on Move Back clicked

            log = ''
            for m in self._tc.iter_messages(self._telegram_user, limit=10):
                log += f'({m.date.ctime()})\n{m.text}\n\n'

                if m.sender.id == self._me.id:
                    continue # We are sender of message thus ignore

                if m.date.timestamp() <= self._last_code_time:
                    continue # Skip old messages

                match = re_search(self._code_pattern, m.text)
                if match:
                    self._last_code_time = m.date.timestamp()
                    return match.group()

            self.log_update.emit(log.rstrip('\n'))

            stime = time() # We need more rapid check, thus, not sleep(5)
            while (time() - stime) < 5:
                if self.isHidden():
                    return # Stop listen
                sleep(0.1)

    @Slot()
    def worker_error(self, error: Exception):
        self.listener = None
        self.switch_widget.emit(5)
        display_popup('Something went wrong. See Details.', error)


class Control(QWidget):
    def __init__(self, stack: QStackedWidget):
        super().__init__()
        self.stack = stack

    @Slot(int)
    def switch_widget(self, w_indx: int):
        requested_w = self.stack.widget(w_indx)
        self.stack.setWindowTitle(requested_w.ui.windowTitle())
        self.stack.setCurrentIndex(w_indx)

    @Slot(str)
    def change_theme(self, cs: str):
        QApplication.instance().setStyleSheet(cs)

        for widget in self.stack.findChildren(QWidget):
            widget.setStyleSheet(cs)


def display_popup(
        text: str, error=None, type_: str='Critical',
        title: str=None, rich: bool=False):

    msg = QMessageBox()

    msg.setIcon(getattr(QMessageBox, type_))
    msg.setWindowTitle(title or f'"{type_}" action occured!')

    if error:
        tb = traceback.format_exception(type(error), error, error.__traceback__)
        msg.setDetailedText(''.join(tb))

    if rich:
        msg.setTextFormat(Qt.RichText)

    msg.setText(text)
    msg.exec()


def catch_exception(exc_type, exc_value, exc_tb):
    error_message = ''.join(traceback.format_exception(
        exc_type, exc_value, exc_tb))

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle('Uncaught Exception')
    msg.setText('An uncaught error occurred!')
    msg.setDetailedText(error_message)
    msg.exec()


def start_app():
    app = QApplication(sys.argv)
    app.setStyle(APP_STYLE or 'Fusion')

    if DARK_MODE is not None and DARK_MODE:
        if DARK_MODE == '1':
            style = DARK_STYLE
        else:
            style = BRIGHT_STYLE
    else:
        style = DARK_STYLE if darkdetect_isDark() else BRIGHT_STYLE

    app.setStyleSheet(style)

    if QFontDatabase.addApplicationFont(':/fonts/inter.ttf') < 0:
        print('Unable to load Inter.ttf!!')
    if QFontDatabase.addApplicationFont(':/fonts/roboto_mono.ttf') < 0:
        print('Unable to load Roboto Mono.ttf!!')

    start_screen_w0 = StartScreen(UIPATH / 'start_screen.ui')
    create_backup_w1 = CreateBackup(UIPATH / 'create_backup.ui')
    create_phrase_w2 = CreatePhrase(UIPATH / 'create_phrase.ui')
    input_birthday_w3 = InputBirthday(UIPATH / 'input_birthday.ui')
    setup_scrypt_w4 = SetupScrypt(UIPATH / 'setup_scrypt.ui')
    account_w5 = Account(UIPATH / 'account.ui')
    open_backup_w6 = OpenBackup(UIPATH / 'open_backup.ui')
    code_w7 = Code(UIPATH / 'code.ui')

    # We will store all of out Widgets in Stack
    stack = AnimatedStackedWidget()
    stack.setFixedSize(start_screen_w0.size())
    stack.setWindowTitle(start_screen_w0.ui.windowTitle())
    stack.setWindowIcon(QIcon(':/images/img/icon.ico'))

    # This class will rule the Widget switch routine
    control = Control(stack)

    start_screen_w0.switch_widget.connect(control.switch_widget)
    create_backup_w1.switch_widget.connect(control.switch_widget)
    create_phrase_w2.switch_widget.connect(control.switch_widget)
    input_birthday_w3.switch_widget.connect(control.switch_widget)
    setup_scrypt_w4.switch_widget.connect(control.switch_widget)
    account_w5.switch_widget.connect(control.switch_widget)
    open_backup_w6.switch_widget.connect(control.switch_widget)
    code_w7.switch_widget.connect(control.switch_widget)

    start_screen_w0.change_theme.connect(control.change_theme)
    create_backup_w1.tg_session.connect(account_w5.set_tg_client)
    input_birthday_w3.open_backup_in_account.connect(account_w5.open_backup)

    account_w5.tg_session.connect(code_w7.set_tg_client)

    open_backup_w6.change_birthday_switch.connect(input_birthday_w3.change_switch_state)
    create_phrase_w2.change_birthday_switch.connect(input_birthday_w3.change_switch_state)
    account_w5.change_birthday_switch.connect(input_birthday_w3.change_switch_state)

    account_w5.reset_ui.connect(create_phrase_w2.reset_ui)
    account_w5.reset_ui.connect(create_backup_w1.reset_ui)

    open_backup_w6.change_scrypt_switch.connect(setup_scrypt_w4.change_switch_state)
    create_phrase_w2.change_scrypt_switch.connect(setup_scrypt_w4.change_switch_state)

    input_birthday_w3.keydata_birthd.connect(account_w5.set_keydata_birthd)
    start_screen_w0.provider.connect(account_w5.set_provider)
    create_phrase_w2.keydata_phrase.connect(account_w5.set_keydata_phrase)
    open_backup_w6.keydata_phrase.connect(account_w5.set_keydata_phrase)
    setup_scrypt_w4.scrypt_n.connect(account_w5.set_scrypt_n)
    setup_scrypt_w4.scrypt_r.connect(account_w5.set_scrypt_r)
    setup_scrypt_w4.scrypt_p.connect(account_w5.set_scrypt_p)
    setup_scrypt_w4.scrypt_dklen.connect(account_w5.set_scrypt_dklen)
    setup_scrypt_w4.scrypt_salt.connect(account_w5.set_scrypt_salt)

    stack.addWidget(start_screen_w0)
    stack.addWidget(create_backup_w1)
    stack.addWidget(create_phrase_w2)
    stack.addWidget(input_birthday_w3)
    stack.addWidget(setup_scrypt_w4)
    stack.addWidget(account_w5)
    stack.addWidget(open_backup_w6)
    stack.addWidget(code_w7)

    for obj in (QPushButton, QComboBox):
        for w in stack.findChildren(obj):
            w.setCursor(QCursor(Qt.PointingHandCursor))

    start_screen_w0.adjustSize()
    stack.setCurrentWidget(start_screen_w0)
    stack.show()

    if LAUNCH_CONSOLE:
        console = PythonConsole()
        console.show()

    sys.excepthook = catch_exception
    sys.exit(app.exec())


if __name__ == '__main__':
    start_app()
