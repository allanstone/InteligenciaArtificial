var math = require('mathjs');
class Maha {

  /**
   * average
   * @param  {Array} ar arreglo con matrices
   * @param  {Int} dim  dimensión de la matriz
   * @return {Matrix}    matrix promedio
   */
  average(ar, dim) {
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

  /**
   * covarianza
   * @param  {Matriz} m Matriz de medias
   * @param  {Array} w Array de matrices con los elementos
   * @return {Matriz}   MAtriz de covarianzas
   */
  covariance(m,w) {
    //creo una matriz inicializada con ceros
    var s;
    var response=math.zeros(m.size().pop(),m.size().pop());
    for (var j = 0; j < m.size(); j++) {
      for (var i = 0; i < m.size(); i++) {
        s=0;
        w.forEach(function (e,k,array) {
            s+=(e._data[j]-m._data[j])*(e._data[i]-m._data[i]);
        });
        response.subset(math.index(j,i),s/data.w1.length);
      }
    }
    return response;
  }

  /**
   * calcula un punto con la formula dada
   * @param  {Vector} x   
   * @param  {Matriz} cov Matriz de covariancias
   * @param  {Matriz} m   Matriz de medias
   * @return {Punto}     Punto en especifico
   */
  calPunto(x,cov,m){
    var fd;
    var xTra = math.transpose(x);
    var covInverse=math.inv(cov);
    var mTra = math.transpose(m);
    fd=(
      math.multiply(
          math.multiply(
            math.multiply(
              xTra,-0.5
              ),covInverse)
          ,x)
      )+(
        math.multiply(
          math.multiply(
            xTra,covInverse
            ),m)
      )-(
        math.multiply(
          math.multiply(
            math.multiply(mTra,0.5)
              ,covInverse),m
          )
        )-(0.5*Math.log(math.det(covInverse)));
    return fd;
  }

};

// var data={
//   w1: [
//             math.matrix([1, 2]), 
//             math.matrix([2, 2]), 
//             math.matrix([3, 1]),
//             math.matrix([2, 3]),
//             math.matrix([3, 2])
//             ],
//   w2: [
//             math.matrix([8, 10]), 
//             math.matrix([9, 8]), 
//             math.matrix([9, 9]),
//             math.matrix([8, 9]),
//             math.matrix([7, 9])
//             ]
// };
var data={
  w1:[
      math.matrix([0.5,10.5]),
      math.matrix([1,12.5]),
      math.matrix([3,10.5]),
      math.matrix([3,12.5]),
      math.matrix([3,14.5]),
      math.matrix([3,18]),
      math.matrix([5,18]),
      math.matrix([5,15]),
      math.matrix([5,14.5]),
      math.matrix([5,13])
    ],
    w2:[
      math.matrix([6,9]),
      math.matrix([8,10]),
      math.matrix([9,11]),
      math.matrix([8.5,12]),
      math.matrix([7,13.5]),
      math.matrix([8,16]),
    ],
}
var M = new Maha();

var m1=M.average(data.w1,data.w1[0].size());
var m2=M.average(data.w2,data.w1[0].size());

var cov1 = M.covariance(m1,data.w1);
var cov2 = M.covariance(m2,data.w2);
console.log(cov1);
console.log(cov2);
// console.log(M.calPunto([1,1],cov1,m1));
// console.log(cov2);
// console.log(m1);




