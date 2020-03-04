import json

from mock import patch, mock_open
from pytest import raises

from src.lib.config.validator import ConfigurationValidator
from src.tests.lib.config.fixtures import *


class TestConfigurationValidator(object):

    def test_config_pathFinded(self, valid_spec):
        with patch("builtins.open",
                   mock_open(read_data=valid_spec)):
            validator = ConfigurationValidator("")
            config = validator.get_config()
            assert config == json.loads(valid_spec)

    def test_invalid_config(self, invalid_spec):
        with patch("builtins.open",
                   mock_open(read_data=invalid_spec)):
            validator = ConfigurationValidator("")

            with raises(ValueError):
                validator.get_config()
    
    def test_valid_constructor(self):
        
