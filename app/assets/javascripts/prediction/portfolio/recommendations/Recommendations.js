import React from 'react';

import ApiContainer from '../../../common/components/ApiContainer';

const Recommendations = ({ recommendations }) => {

  let element,
    data = recommendations.data;

  if (data) {

    let labelType = (trade) => {
        return (trade === 'sell') ? 'btn-label--sell' : ((trade === 'buy') ? 'btn-label--buy' : 'btn-label--hold');
    };

    element = <ul>
      { data.map((item, index) => {
          if (index < 3) {
            return <li key={index}>
              <label
                className={"btn-label " + labelType(item.trade)}>{item.trade.toUpperCase()}</label>
              <span className="text-small">{item.asset}</span>
            </li>
          }
        }
      )}
    </ul>
  }

  return <ApiContainer {...{
    isFetching: recommendations.isFetching,
    isFailed: recommendations.isFailed,
    element: element
  }}></ApiContainer>
};

export default Recommendations;