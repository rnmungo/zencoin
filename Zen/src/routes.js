// Dependencies
import React from 'react';
//import { Component, Redirect } from 'react-dom';
import { Route, Switch } from 'react-router-dom';

// Components
import App from './components/App';
import Login from './components/User/Login';
import Transfer from './components/Transfer';
import Password from './components/User/Password';
import Panel from './components/Panel';
import Welcome from './components/Welcome';
import Page404 from './components/Errors/404';

/*
class ProtectedRoute extends Component {
  render() {
    const { component: Component, ...props } = this.props
    return (
      <Route
        {...props}
        render={props => (
          this.state.authenticated ?
            <Component {...props} /> :
            <Redirect to='/login' />
        )}
      />
    )
  }
}*/

const AppRoutes = () =>
	<App>
		<Switch>
			<Route exact path="/" render={() => <Welcome />} />
			<Route exact path="/panel" render={() => <Panel />} />
			<Route exact path="/transfer" render={() => <Transfer />} />
			<Route exact path="/login" render={() => <Login />} />
			<Route exact path="/password" render={() => <Password />} />
			<Route render={() => <Page404 />} />
		</Switch>
	</App>;

export default AppRoutes;
