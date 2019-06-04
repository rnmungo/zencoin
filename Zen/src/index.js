// Dependencies
import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import * as serviceWorker from './serviceWorker';

// Routes
import AppRoutes from './routes';

// Assets
import './index.css';

render(
	<Router>
		<AppRoutes />
	</Router>,
	document.getElementById('root')
);
serviceWorker.unregister();
