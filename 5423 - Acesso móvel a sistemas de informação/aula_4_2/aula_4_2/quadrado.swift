//
//  quadrado.swift
//  aula_4_2
//
//  Created by Gonçalo Feliciano on 18/10/2024.
//
import Foundation

class Quadrado{
    private var _lado: Float{
        
        willSet{
            print("o valor de lado vai mudar de \(self.lado) para \(newValue)")
        }
        //set
        
        didSet{
            print("o valor de lado mudou de \(oldValue) para \(self.lado)")
        }
        
    }
    
    var lado: Float{
        
        set{
            _lado = newValue
        }
        
        get{
            return _lado
        }
    }
    
    
    var area: Float{
        set{
            self.lado = sqrt(newValue)
        }
        
        get{
            return pow(lado, 2)
        }
    }
    
    
     var perimetro: Float{
         set{
             self.lado = newValue / 4
         }
         
         get{
             return lado * 4
         }
     }
    
    
    init(lado: Float) {
        self._lado = lado
    }

    
 
    
}
