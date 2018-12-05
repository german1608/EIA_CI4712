Feature: Manejar Medidas

    Scenario: Eliminar Medida
        Given Vista de agregar medidas
        When Mando el form con datos validos de medida
        When Quiero eliminar una medida
        Then La medida no aparece en la lista

    Scenario: Agregar Medida
        Given Vista de agregar medidas 
        When Mando el form con datos validos de medida
        Then La medida agregada aparece en la lista
  
    Scenario: Editar Medida
        Given La medida agregada aparece en la lista
        When Se quiere editar una medida
        And Edito con datos validos
        Then La medida editada aparece en la lista