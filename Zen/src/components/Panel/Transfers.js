import React, { Component } from 'react';
import PropTypes from 'prop-types';
import '../Global/css/bootstrap.min.css';


class Transfers extends Component {

    static propTypes = {
        transfers: PropTypes.array.isRequired,
        accountId: PropTypes.string
    }

    render () {
      const { transfers, accountId } = this.props;
      if (transfers.length > 0) {
        return (
          <div className="container border rounded text-center mt-3">
            <h3>Últimos Movimientos</h3>
            <table className="table table-sm table-hover table-light table-responsive-sm text-center border">
              <thead>
                <tr>
                  <th scope="col" className="border-top border-bottom">Fecha / Hora</th>
                  <th scope="col" className="border-top border-bottom">Motivo</th>
                  <th scope="col" className="border-top border-bottom">Monto</th>
                </tr>
              </thead>
              <tbody>
                {transfers.map((trans, key) => {
                  return (
                    <tr key={key}>
                      <td className="border-0">
                        {trans.created_at}
                      </td>
                      <td className="border-0">
                        {trans.from_account.id === accountId ? 'Transferencia a cuenta #' + trans.to_account.number : 'Acreditación de cuenta #' + trans.from_account.number}
                      </td>
                      <td className="border-0">
                        {trans.from_account.id === accountId ? '- ' + trans.total.toString() + ' ZenCoins' : trans.total.toString() + ' ZenCoins'}
                      </td>
                    </tr>
                    )
                })}
              </tbody>
            </table>
          </div>
        );
      }
      else {
        return (
          <div className="container border rounded text-center mt-3">
            <h3>Últimos Movimientos</h3>
            <p>Cargando...</p>
          </div>
        );
      }
    }
}

export default Transfers;
