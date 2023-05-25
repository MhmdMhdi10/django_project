import {
    SIGNUP_FAIL, SIGNUP_SUCCESS,
    ACTIVATION_SUCCESS,ACTIVATION_FAIL,
    SET_AUTH_LOADING,REMOVE_AUTH_LOADING,
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

        case ACTIVATION_SUCCESS:
        case ACTIVATION_FAIL:
            return {
                ...state
            }
        case SIGNUP_SUCCESS:
        case SIGNUP_FAIL:
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