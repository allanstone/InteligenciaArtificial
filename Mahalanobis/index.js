var math = require('mathjs');
var dim=2;
var w1=[
          math.matrix([1, 2]), 
          math.matrix([2, 2]), 
          math.matrix([3, 1]),
          math.matrix([2, 3]),
          math.matrix([3, 2])
          ];
var w2=[
          math.matrix([8, 10]), 
          math.matrix([9, 8]), 
          math.matrix([9, 9]),
          math.matrix([8, 9]),
          math.matrix([7, 9])
          ];

/**
 * average
 * @param  {Array} ar arreglo con matrices
 * @param  {Int} dim  dimensión de la matriz
 * @return {Matrix}    matrix promedio
 */
function average(ar, dim) {
  var aux=[];
    function cal(ar, r){
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
  for (var i = 0; i < dim; i++) {
    var a=cal(ar,i)
    aux.push(a);
  }
  return math.matrix(aux);
}


var m1=average(w1,dim);
var m2=average(w2,dim);

console.log(m1);
console.log(m2);
