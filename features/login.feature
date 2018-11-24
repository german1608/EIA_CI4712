Feature: Login form

  Scenario: Hacer login de forma exitosa

    Given Usuario loggeado 
    And Usuario registrado 
    When Introduzco los datos correctamente
    Then Me redirigen a la vista de registro

  