import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../Global/css/bootstrap.min.css';


class Cotization extends Component {

    static propTypes = {
        conversions: PropTypes.array.isRequired,
    }

    render () {
      const { conversions } = this.props;
      if (conversions.length > 0) {
        return (
          <div className="container border rounded text-center mt-3">
            <h3>Cotizaciones</h3>
            <p>Las cotizaciones son meramente informativas</p>
            <table className="table table-sm table-hover table-light text-center border">
              <thead>
                <tr>
                  <th scope="col" className="border-top border-bottom">Moneda</th>
                  <th scope="col" className="border-top border-bottom">Valor</th>
                </tr>
              </thead>
              <tbody>
                {conversions.map((conversion, key) => <tr key={key}><td className="border-0">{conversion.to_currency.name}</td><td className="border-0">{conversion.rate}</td></tr>)}
              </tbody>
            </table>
          </div>
        );
      }
      else {
        return (
          <div className="container border rounded text-center mt-3">
            <h3>Cotizaciones</h3>
            <p>Las cotizaciones son meramente informativas</p>
            <p>Sin resultados...</p>
          </div>
        );
      }
    }
}

export default Cotization;
