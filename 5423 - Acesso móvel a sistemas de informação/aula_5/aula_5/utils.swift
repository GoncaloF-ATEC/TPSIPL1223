//
//  utils.swift
//  aula_5
//
//  Created by Gonçalo Feliciano on 22/10/2024.
//


enum Grau{
    case BSc
    case MSc
    case PHd
    
}


extension Array<Int>{
    
    var avg: Float{
        var sum = 0
        
        self.forEach { elm in
            sum += elm 
        }
    
        return Float(sum)/Float(self.count)
        
    }
    
}


