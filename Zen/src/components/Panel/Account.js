import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../Global/css/bootstrap.min.css';
import '../Global/css/Panel.css';


class Account extends Component {

    static propTypes = {
        account: PropTypes.object.isRequired,
    }

    render () {
      const { account } = this.props;
      return (
        <div className="container border rounded text-center mt-3">
          <h3>Cuenta #{account.number}</h3>
          <h2>Saldo {Math.round(account.saldo, 5)} ZenCoins</h2>
        </div>
      );
    }
}

export default Account;
