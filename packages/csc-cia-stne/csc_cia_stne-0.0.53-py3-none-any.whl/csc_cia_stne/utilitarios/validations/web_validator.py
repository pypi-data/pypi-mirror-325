from pydantic import BaseModel, field_validator


class InitParamsValidator(BaseModel):
    """
    Classe para validar os parâmetros de inicialização.
    Atributos:
        model (str): O modelo a ser utilizado. Deve ser uma string e pode ser 'selenium' ou 'boticy'.
        headless (bool): Define se o navegador será executado em modo headless.
        disable_gpu (bool): Define se a aceleração de hardware será desabilitada.
        no_sandbox (bool): Define se o sandbox do navegador será desabilitado.
        timeout (int): O tempo limite para a execução de operações.
    Métodos:
        check_str_basic(cls, value, info): Valida se o valor é uma string não vazia e se está dentro das opções permitidas.
        check_bool_input(cls, value, info): Valida se o valor é um booleano.
    """
    
    model:str
    headless:bool
    disable_gpu:bool
    no_sandbox:bool
    timeout:int

    @field_validator('model')
    def check_str_basic(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O parametro 'model' deve ser uma string e não um {type(value)} e não vazio")
        if value.upper() not in ['SELENIUM', 'BOTCITY']:
            raise ValueError(f"O parametro 'model' deve ser 'selenium' ou 'boticy' e não {value}")
        return value
    
    @field_validator('timeout')
    def check_int_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O parametro 'model' deve ser um int e não um {type(value)} e não vazio")
        return value
    
    @field_validator('headless','disable_gpu','no_sandbox')
    def check_bool_input(cls, value, info):
        if not isinstance(value, bool):
            raise ValueError(f"O parametro '{info.field_name}' deve ser um boleano")
        
        return value
    

class ClickOnScreenValidator():
    """
    Classe para validar os parâmetros 'target' e 'timeout' da classe ClickOnScreenValidator.
    Atributos:
        target (str): O alvo a ser validado.
    Métodos:
        check_str_basic(value, info): Valida se o valor do parâmetro 'target' é uma string não vazia.
    """
    target:str

    @field_validator('target')
    def check_str_basic(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O parametro 'target' deve ser uma string e não um {type(value)} e não vazio")
        return value

class InputValueValidator():
    """
    Classe para validar os valores de entrada.
    Atributos:
        target (str): O valor de destino a ser validado.
        clear (bool): Indica se o valor deve ser limpo.
    Métodos:
        check_str_basic(value, info): Valida se o valor fornecido é uma string não vazia.
        check_bool_input(value, info): Valida se o valor fornecido é um booleano.
    """
    target:str
    clear:bool

    @field_validator('target')
    def check_str_basic(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O parametro 'target' deve ser uma string e não um {type(value)} e não vazio")
        return value

    @field_validator('clear')
    def check_bool_input(cls, value, info):
        if not isinstance(value, bool):
            raise ValueError(f"O parametro 'clear' deve ser um boleano")
        return value
    

class SelectValueValidator():
    """
    Classe para validação de valores do seletor.
    Atributos:
        target (str): O valor do seletor.
    Métodos:
        check_str_basic(value, info): Valida se o valor do seletor é uma string não vazia.
    """

    target:str

    @field_validator('target')
    def check_str_basic(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O parametro 'target' deve ser uma string e não um {type(value)} e não vazio")
        return value