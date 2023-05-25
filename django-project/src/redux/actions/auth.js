import {
    SIGNUP_SUCCESS, SIGNUP_FAIL,
    ACTIVATION_SUCCESS, ACTIVATION_FAIL,
    SET_AUTH_LOADING, REMOVE_AUTH_LOADING,
} from "./types";
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
        } else {
            dispatch({
                type: SIGNUP_FAIL,
            });
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
        } else {
            dispatch({
               type: ACTIVATION_FAIL
            });
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
    }

};