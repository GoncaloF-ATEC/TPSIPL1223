//
//  main.swift
//  aula3
//
//  Created by Gonçalo Feliciano on 02/10/2024.
//

import Foundation



/*
 
 var
 let
 
 tuplos
 
 if, else
 
 while
 
 switch
    
 for
 
 funcs
 
 */

/*
 
 opts
 
 */



var ano:String? // int ano; printf("%d", ano);

// nil <-> null
ano = "Gonçalo"

//var ano2 = ano! + ", 2024"


//print(ano2)


ano = "Gonçalo"
if let ano = ano { // <-> if let ano = ano
    
    print(ano)
}else{
    
    print("Sem Valor")
}



ano = "str"
print(ano ?? "Sem valor 2", terminator: " - End - ")

print("")


/*
 
 ! -
 
 ?? -
 
 
 
 if let
 
 guard let
 
 
 
 */


var fotoURL: String?

print(fotoURL ?? "foto pre definida")


print("........")
func teste(nome:String? = nil, ano:Int? = nil){
    
    if let ano = ano { // <-> if let ano = ano
        
        print(ano)
    }else{
        
        print("Sem Valor")
    }
    
    
    print("---- codigo 1 ----")
    
    guard let abcd = nome, !abcd.isEmpty else{
        print("Sem Valor")
        return
    }
    
    print("---- codigo 2 ----")
    print(abcd)
  
    
}

teste(nome: "Gonçalo")
teste(nome: "")
teste()




func media(nota1:Float? = nil, nota2:Float? = nil) -> Float{
    
    guard let nota1 = nota1 else{
        // calc nota 1
        
        let nt1:Float = 10.0
        
        return media(nota1: nt1, nota2: nota2)
         
    }
    
    guard let nota2 = nota2 else{
        
        let nt2:Float = 10.0
        return media(nota1: nota1, nota2: nt2)
    }
    
    return (nota1 + nota2)/2.0
    
}


print(media(nota1: 20, nota2: 20))
print(media(nota2: 20))
print(media(nota1: 20))
print(media())


print("..................")

var dados = readLine()
print(dados)

