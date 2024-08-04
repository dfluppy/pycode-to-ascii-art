import base64
import cv2

class PyCodeTOAscii:
    SET_ASCII_CHARS: tuple[str] = ('@', '*', ' ', ' ',)
    SET_SCALE: int = 50
    SET_THRESHOLD = 0

    def __init__(self,
                 img: str,
                 ascii_chars: tuple[str],
                 scale: int,
                 width: int,
                 height: int,
                 invert: bool,
                 add_exec: bool,
                 pycode: str,
                 threshold: int = SET_THRESHOLD):

        self.img = img
        self.ascii_chars = ascii_chars
        self.scale = scale
        self.width = width
        self.height = height
        self.invert = invert
        self.add_exec = add_exec
        self.pycode = pycode
        self.threshold = threshold

    @staticmethod
    def __checker(value, defaulf):
        """
        Установка значений в локальные атрибуты класса
        :param value: значение юзера
        :param defaulf: дефолтные значения
        :return: значения (int / bool / tuple)
        """
        return value if value else defaulf

    def __get_char_bright(self, brightness_pixel: int, ascii_chars: tuple[str]) -> str:
        """
        Метод для получения подходящего символа под яркость пикселя
        :param brightness_pixel: `int` текущего пикселя
        :param ascii_chars: `tuple` кортеж с набором допустимых символов
        :return: подходящий символ под яркость пикселя
        """

        bright_coef = brightness_pixel / 255
        index_char = int((len(ascii_chars) - 1) * bright_coef)

        return ascii_chars[index_char]

    def generate_ascii_art(self, binary_image) -> str:
        """
        Метод для генерации ASCII арта
        :return: `str` сгенерированный ASCII арт
        """

        image = cv2.imread(self.img)

        SET_HEIGHT, SET_WIDTH, _ = image.shape

        if self.invert:
            self.ascii_chars = tuple(reversed(self.__checker(self.ascii_chars, self.SET_ASCII_CHARS)))
        else:
            self.ascii_chars = tuple(self.__checker(self.ascii_chars, self.SET_ASCII_CHARS))

        raw_pycode = self.pycode if self.add_exec and self.pycode else ''

        try:
            self.pycode = 'bcode = """\n' + base64.b64encode(raw_pycode.encode()).decode()
        except AttributeError as ae:
            print(ae)

        self.width = int(self.__checker(self.width, SET_WIDTH))
        self.height = int(self.__checker(self.height, SET_HEIGHT))
        self.scale = int(self.__checker(self.scale, self.SET_SCALE))

        aspect_ratio = self.height / self.width

        scale_size = self.scale / 100
        new_width = int(self.width * scale_size)
        new_height = int((aspect_ratio * new_width * 0.6) * scale_size)

        prepared_img = cv2.resize(binary_image, (new_width, new_height), interpolation=cv2.INTER_AREA)

        ascii_art = ''
        for row in prepared_img:
            for brightness_pixel in row:
                ascii_art += self.__get_char_bright(brightness_pixel, self.ascii_chars)
            ascii_art += '\n'

        exec_code = f'"""\nexec(__import__("base64").b64decode(bcode))'

        return self.pycode + ascii_art + exec_code if self.add_exec else ascii_art
