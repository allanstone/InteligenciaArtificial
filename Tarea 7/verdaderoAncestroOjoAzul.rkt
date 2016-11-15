;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname verdaderoAncestroOjoAzul) (read-case-sensitive #t) (teachpacks ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "show-queen.ss" "teachpack" "htdp") (lib "image.ss" "teachpack" "2htdp") (lib "universe.ss" "teachpack" "2htdp") (lib "batch-io.ss" "teachpack" "2htdp")) #f)))
;Verdadero ancestro ojo azul
(define (verdadero-ancestro-ojo-azul? fam)
  ;Se verifica si es un Hijo 
  (if (hijo? fam)
  ;Si es un hijo buscamos en la madre o padre      
      (or
       ;MADRE
          (if(hijo? (hijo-madre fam))
             ;Si tiene madre: Si tiene ojos azules "TRUE" 
             (if (equal? (hijo-ojos (hijo-madre fam)) 'blue) true
             ;Si no tiene ojos azules Realizamos nueva Busqueda apartir de la MADRE
             (verdadero-ancestro-ojo-azul? (hijo-madre fam)))
            ;Si no tiene madre "FALSE"
             false)
        ;PADRE
          (if(hijo? (hijo-padre fam))
             ;Si tiene padre: Si tiene ojos azules "TRUE" 
             (if (equal? (hijo-ojos (hijo-padre fam)) 'blue) true
             ;Si no tiene ojos azules Realizamos nueva Busqueda apartir del PADRE
             (verdadero-ancestro-ojo-azul? (hijo-padre fam)))
             ;Si no tiene padre "FALSE"
             false)
  ;Si se cumple que es hijo "FALSE"
   )false))

(check-expect (verdadero-ancestro-ojo-azul?  Carl) false)
(check-expect (verdadero-ancestro-ojo-azul?  Gustav) true)
(check-expect (verdadero-ancestro-ojo-azul?  Robert) true)
(check-expect (verdadero-ancestro-ojo-azul?  Eva) true)
(check-expect (verdadero-ancestro-ojo-azul?  empty) false)

