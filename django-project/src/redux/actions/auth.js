import {
    SIGNUP_SUCCESS, SIGNUP_FAIL,
    ACTIVATION_SUCCESS, ACTIVATION_FAIL,
    SET_AUTH_LOADING, REMOVE_AUTH_LOADING,
    LOGIN_SUCCESS, LOGIN_FAIL,
    USER_LOADED_SUCCESS,USER_LOADED_FAIL,

} from "./types";
import {setAlert} from "./alert";
import axios from "axios";

export const signup = (first_name, last_name, email, password, re_password) => async (dispatch) => {

    dispatch({
       type: SET_AUTH_LOADING
    });

    const headers = {
        "Content-Type": "application/json",
    };

    console.log(headers)

    const body = JSON.stringify({
        first_name,
        last_name,
        email,
        password,
        re_password
    });

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/users`, body, {
            headers,
        });

        if (res.status === 201) {
            dispatch({
                type: SIGNUP_SUCCESS,
                payload: res.data,
            });
            dispatch(setAlert('signup was successful', 'green'))
        } else {
            dispatch({
                type: SIGNUP_FAIL,
            });
            dispatch(setAlert('signup Failed', 'red'))
        }
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
    } catch (err) {
        dispatch({
            type: SIGNUP_FAIL,
        });
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
        dispatch(setAlert('signup failed', 'red'))
    }
};

export const load_user = () => async dispatch => {
    if(localStorage.getItem('access')){
        const config = {
            headers: {
                'Authorization': `JWT ${localStorage.getItem('access')}`,
                'Accept': 'application/json'
            }
        };
        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/users/me/`, config);
            if (res.status === 200) {
                dispatch({
                    type: USER_LOADED_SUCCESS,
                    payload: res.data
                });
            } else {
                dispatch({
                    type: USER_LOADED_FAIL
                });
            }
        }catch (err){
            dispatch({
                type: USER_LOADED_FAIL
            });
        }
    } else {
        dispatch({
            type: USER_LOADED_FAIL
        });
    }
};

export const login = (email, password) => async dispatch => {
    dispatch({
       type: SET_AUTH_LOADING
    });

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const  body = JSON.stringify({
        email,
        password
    });

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/jwt/create/`, body, config)

        if (res.status === 200) {
            dispatch({
                type: LOGIN_SUCCESS,
                payload: res.data
            });
            dispatch(load_user());

            dispatch({
                type:REMOVE_AUTH_LOADING,
            });
            dispatch(setAlert('login successful', 'green'));
        } else {
            dispatch({
                type:LOGIN_FAIL
            });
            dispatch({
                type: REMOVE_AUTH_LOADING
            });
            dispatch(setAlert('login failed', 'red'))
        }

    } catch(err){
        dispatch({
            type:LOGIN_FAIL
        });
        dispatch({
            type: REMOVE_AUTH_LOADING
        });
        dispatch(setAlert('login failed', 'red'))
    }

};

export const activate = (uid, token) => async dispatch => {
    dispatch({
       type: SET_AUTH_LOADING
    });



    const config = {
        headers:{
            'Content-type': 'application/json'
        }
    };

    const body = JSON.stringify({
        uid,
        token
    });

    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/auth/users/activate`)

        if (res.status === 204) {
            dispatch({
               type: ACTIVATION_SUCCESS
            });
            dispatch(setAlert('activation was successful', 'green'))
        } else {
            dispatch({
               type: ACTIVATION_FAIL
            });
            dispatch(setAlert('activation Failed', 'red'))
        }
        dispatch({
           type: REMOVE_AUTH_LOADING
        });

    } catch (err){
        dispatch({
            type: ACTIVATION_FAIL
        });
        dispatch({
           type: REMOVE_AUTH_LOADING
        });
        dispatch(setAlert('activation Failed', 'red'))
    }

};

