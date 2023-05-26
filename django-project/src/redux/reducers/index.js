import { combineReducers } from 'redux';
import Auth from './auth';
import Alert from "./alert";

export default combineReducers({
    Auth,
    Alert
})