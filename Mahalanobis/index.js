var math = require('mathjs');

var w1 = [
          math.matrix([1, 2]), 
          math.matrix([2, 2]), 
          math.matrix([3, 1]),
          math.matrix([2, 3]),
          math.matrix([3, 2])
          ];

/**
 * average
 * @param  {Array} ar arreglo con matrices
 * @param  {Int} r  indice a calcular el promedio
 * @return {Int}    promedio del renglon
 */
function average(ar, r) {
    var prom=0;
    ar.forEach(function (m, index, array) {
        m.forEach(function(e,i,matrix) {
            if (i==r) {
                prom+=e;
            }
        });
    });
    return prom/ar.length;
}

    