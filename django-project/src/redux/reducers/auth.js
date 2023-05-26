import {
    SIGNUP_FAIL, SIGNUP_SUCCESS,
    ACTIVATION_SUCCESS,ACTIVATION_FAIL,
    SET_AUTH_LOADING,REMOVE_AUTH_LOADING,
    LOGIN_SUCCESS,LOGIN_FAIL,
    USER_LOADED_SUCCESS, USER_LOADED_FAIL,
    } from "../actions/types";

const initialState = {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    is_authenticated: null,
    user: null,
    loading: false,

}

export default function (state = initialState, action) {
    const { type, payload} = action;
    switch (type){
        case SET_AUTH_LOADING:
            return {
                ...state,
                loading: true
            }
        case REMOVE_AUTH_LOADING:
            return {
                ...state,
                loading: false
            }
        case USER_LOADED_SUCCESS:
            return {
                ...state,
                user:payload
            }
        case USER_LOADED_FAIL:
            return {
                ...state,
                user: null
            }
        case LOGIN_SUCCESS:
            localStorage.setItem('access', payload.access);
            localStorage.setItem('refresh', payload.refresh);
            return {
                ...state,
                is_authenticated: true,
                access: localStorage.getItem('access'),
                refresh: localStorage.getItem('refresh')
            }

        case ACTIVATION_SUCCESS:
        case ACTIVATION_FAIL:
            return {
                ...state
            }
        case SIGNUP_SUCCESS:
        case SIGNUP_FAIL:
        case LOGIN_FAIL:
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
            return {
                ...state,
                access: null,
                refresh: null,
                is_authenticated: false,
                user: null
            }
        default:
            return state
    }
}