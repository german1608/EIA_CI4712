var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

// Componente que saluda al usuario la primera vez que se loggea
function Welcome(props) {
    var bienvenida = void 0;
    // Condicional que permite dar la bienvenidad si es la primera vez que se loggea
    if (props.proyectoSeleccionado === '') {
        bienvenida = React.createElement(
            'div',
            { className: 'mensajeEntrada content' },
            React.createElement(
                'h1',
                null,
                'Bienvenido, ',
                props.nombre
            ),
            React.createElement(
                'h2',
                null,
                'Selecciona un proyecto'
            )
        );
    } else {
        bienvenida = React.createElement(
            'h1',
            null,
            'Selecciona un proyecto'
        );
    };
    return bienvenida;
}

// Clase que maneja la seleccion de proyecto

var SeleccionProyectoForm = function (_React$Component) {
    _inherits(SeleccionProyectoForm, _React$Component);

    function SeleccionProyectoForm(props) {
        _classCallCheck(this, SeleccionProyectoForm);

        var _this = _possibleConstructorReturn(this, (SeleccionProyectoForm.__proto__ || Object.getPrototypeOf(SeleccionProyectoForm)).call(this, props));

        _this.state = { value: _this.props.nombreProyecto };

        _this.handleChange = _this.handleChange.bind(_this);
        _this.handleSubmit = _this.handleSubmit.bind(_this);
        return _this;
    }

    // Maneja el evento en el cual se selecciona un proyecto


    _createClass(SeleccionProyectoForm, [{
        key: 'handleChange',
        value: function handleChange(event) {
            this.setState({ value: event.target.value });
        }

        // Maneja el evento cuando se confirma el proyecto

    }, {
        key: 'handleSubmit',
        value: function handleSubmit(event) {
            alert('El proyecto seleccionado fue: ' + this.state.value);
        }
    }, {
        key: 'render',
        value: function render() {
            var proyectosActuales = this.props.listaProyectos;
            var listaProyectos = proyectosActuales.map(function (proyecto) {
                return React.createElement(
                    'option',
                    { value: proyecto.pk },
                    proyecto.titulo
                );
            });

            return React.createElement(
                'form',
                { className: 'content', onSubmit: this.handleSubmit },
                React.createElement(
                    'label',
                    { htmlFor: '' },
                    React.createElement(
                        'select',
                        { className: 'custom-select', value: this.state.value, onChange: this.handleChange },
                        React.createElement(
                            'option',
                            { value: true },
                            'Proyecto a editar'
                        ),
                        listaProyectos
                    )
                ),
                React.createElement('input', { className: 'btn btn-primary botonSeleccionar', type: 'submit', value: 'Elegir' })
            );
        }
    }]);

    return SeleccionProyectoForm;
}(React.Component);

// Funcion que renderiza toda la aplicacion


function App(props) {
    return React.createElement(
        'div',
        { className: 'seleccionarUnProyecto' },
        React.createElement(Welcome, { nombre: props.nombreCompleto, proyectoSeleccionado: '' }),
        React.createElement(SeleccionProyectoForm, { nombreProyecto: '', listaProyectos: props.contextoProyectos })
    );
}

// Con ajax se obtiene el json que contiene informacion del back 
// por ejemplo con la lista de proyectos
$.ajax({
    url: "proyectos/",
    type: "GET",
    dataType: "json",
    contentType: "application/json",
    success: function success(json) {
        // Se obtiene la lista de proyectos asociado
        // al usuario asociado en ese momento
        var listaProyectos = json['proyectos'];
        // Se obtiene del json el usuario que esta 
        // loggeado en el momento
        var usuarioLoggeado = json['usuario'][0];
        ReactDOM.render(React.createElement(App, { nombreCompleto: usuarioLoggeado['first_name'], contextoProyectos: listaProyectos }), document.getElementById('seleccionarProyecto'));
    }
});