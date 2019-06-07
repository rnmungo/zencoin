import React, { Component } from 'react';
import logo from '../Global/img/money.png';
import {Link} from 'react-router-dom';
import PropTypes from 'prop-types';
import '../Global/css/bootstrap.min.css';
import '../Global/css/Panel.css';


class Navbar extends Component {

    static propTypes = {
        username: PropTypes.string.isRequired
    }

    render () {
      const { username } = this.props;
      return (
        <nav className="navbar navbar-expand-md navbar-light bg-white shadow-sm">
            <div className="container">
                <Link to="/"><img src={logo} className="img-fluid icon mx-2 rounded-circle shadow" alt={logo} /></Link>
                <Link className="navbar-brand" to="/panel">ZenCoin</Link>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="{{ __('Toggle navigation') }}">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item">
                            <Link className="nav-link" to="/transfer">
                                Transferencia Inmediata
                            </Link>
                        </li>
                    </ul>
                    <ul className="navbar-nav ml-auto">
                        <li className="nav-item active"><a className="nav-link" href="#">{username}</a></li>
                        <li className="nav-item">
                            <a href="#" className="nav-link" onClick={this.props.handleLogOut}>
                                Cerrar Sesión
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
      );
    }
}

export default Navbar;
