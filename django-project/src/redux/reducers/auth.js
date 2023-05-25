import {SIGNUP_FAIL, SIGNUP_SUCCESS} from "../actions/types";

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