Feature: Login form
    Background:
        Given Usuario registrado

    Scenario: Hacer login de forma exitosa
        Given Usuario loggeado 
        When Introduzco los datos correctamente
        Then Me redirigen a la vista de registro

  