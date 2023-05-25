import { SIGNUP_SUCCESS, SIGNUP_FAIL } from "./types";
import axios from "axios";

export const signup = (first_name, last_name, email, password, re_password) => async (dispatch) => {





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
  } catch (err) {
    dispatch({
      type: SIGNUP_FAIL,
    });
  }
};

