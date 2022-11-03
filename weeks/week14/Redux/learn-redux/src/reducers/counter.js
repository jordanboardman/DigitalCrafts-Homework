const counterReducer = (state, action) => {
  if (state === undefined) {
    state = {
      payload: 0,
    };
  }
  switch (action.type) {
    case "INCREMENT":
      return {
        ...state,
        payload: state.payload + action.payload,
      };
    case "DECREMENT":
      return {
        ...state,
        payload: state.payload - action.payload,
      };
    default:
      return state;
  }
};

export default counterReducer;
