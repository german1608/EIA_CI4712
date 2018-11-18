# -- FILE: features/buscarMarco.feature
Feature: Buscar un marco metodologico, teorico y juridico dentro un proyecto

    Scenario: Se busca un marco metodologico a un proyecto
        Given: El usuario se encuentra en la vista que muestra la tabla de marcos metodologico
        When: El usuario escribe una palabra clave en el input para buscar
        Then: Se muestran en la tabla aquellos marcos metodologico con sus proyectos que coinciden con la palabra clave

    Scenario: Se busca un marco juridico a un proyecto
        Given: El usuario se encuentra en la vista que muestra la tabla de marcos juridico
        When: El usuario escribe una palabra clave en el input para buscar
        Then: Se muestran en la tabla aquellos marcos juridico con sus proyectos que coinciden con la palabra clave

    Scenario: Se busca un marco teorico a un proyecto
        Given: El usuario se encuentra en la vista que muestra la tabla de marcos teorico
        When: El usuario escribe una palabra clave en el input para buscar
        Then: Se muestran en la tabla aquellos marcos teorico con sus proyectos que coinciden con la palabra clave