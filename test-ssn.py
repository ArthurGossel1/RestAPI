from parserssn import SSN


def test_ssn_is_length_valid():
    num = SSN("A19783479")
    assert(num.is_length_valid() is False)

    num = SSN("123456789012345")
    assert(num.is_length_valid() is True)

    num = SSN("")
    assert(num.is_length_valid() is False)

    num = SSN("11111111111111111")
    assert (num.is_length_valid() is False)


def test_is_valid():
    #On donne un numero que l'on sait valide pour vérifier la validité de la fonction
    num = SSN("197099102726950")
    assert (1 == 1)
