import React, { Component } from 'react';
import PropTypes from 'prop-types';
import logo from '../Global/img/money.png';
import '../Global/css/Login.css';
import '../Global/css/bootstrap.min.css';
import {Link} from 'react-router-dom';

class Welcome extends Component {
  static propTypes = {
    auth: PropTypes.bool.isRequired
  }
  render () {
    return (
      <div className="Content">
          <img src={logo} className="Logo" alt="logo" />
          <h2 className="mt-3">Bienvenido a ZenCoin</h2>
          {
            this.props.auth
              ? <Link to={'/panel'} className="btn btn-info shadow-sm mt-3">Panel</Link>
              : <Link to={'/login'} className="btn btn-secondary shadow-sm mt-3">Iniciar Sesión</Link>
          }

      </div>
    );
  }
}

export default Welcome;
