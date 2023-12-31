import { PRODUIT_LIST_SUCCESS,
    PRODUIT_LIST_FAIL,
    PRODUIT_LIST_REQUEST,
    PRODUIT_DETAILS_SUCCESS,
    PRODUIT_DETAILS_FAIL,
    PRODUIT_DETAILS_REQUEST,

    PRODUCT_CREATE_REVIEW_FAIL,
    PRODUCT_CREATE_REVIEW_REQUEST,
    PRODUCT_CREATE_REVIEW_SUCCESS,
} from '../constants/produitConstant';
import  axios  from 'axios';


export const listeProduits = (keyword = '') => async (dispatch) => {
    try{
        dispatch({ type : PRODUIT_LIST_REQUEST })

        const { data } = await axios.get(`/api/products/${keyword}`)

        dispatch({
            type : PRODUIT_LIST_SUCCESS,
            payload : data
    })
    }catch(error) {
        dispatch({
            type : PRODUIT_LIST_FAIL, 
            payload : error.response && error.response.body && error.response.data.detail
            ? error.response.data.detail
            : error.message,
        
        })

    }
}

export const listeProduitsDetails = (id) => async (dispatch) => {
    try{
        dispatch({ type : PRODUIT_DETAILS_REQUEST })

        const { data } = await axios.get(`/api/products/${id}/`)

        dispatch({
            type : PRODUIT_DETAILS_SUCCESS,
            payload : data
    })
    }catch(error) {
        dispatch({
            type : PRODUIT_DETAILS_FAIL, 
            payload : error.response && error.response.body && error.response.data.detail
            ? error.response.data.detail
            : error.message 
        
        })

    }
}

export const createProductReview = (productId, review) => async (dispatch, getState) =>{
    try{
        dispatch({
            type: PRODUCT_CREATE_REVIEW_REQUEST
        })

        const {
            userLogin: {userInfo},

        }= getState()

        const config = {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${userInfo.token}`,
            }
        }

        const{ data } = await axios.post(
            `/api/products/${productId}/reviews/`,
            review,
            config,
        )
        dispatch(
            {
                type: PRODUCT_CREATE_REVIEW_SUCCESS,
                payload: data,
            }
        )
    }catch (error) {
        dispatch({
            type: PRODUCT_CREATE_REVIEW_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                :error.message,
        })
    }
}