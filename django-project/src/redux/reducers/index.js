import { combineReducers } from 'redux';
import Auth from './auth';
import Alert from "./alert";
import Categories from "./categories";
import Cart from './cart';
import Shipping from "./shipping";
import Coupons from "./coupons";
import Orders from "./orders";


export default combineReducers({
    Auth,
    Alert,
    Categories,
    Cart,
    Shipping,
    Coupons,
    Orders,
})