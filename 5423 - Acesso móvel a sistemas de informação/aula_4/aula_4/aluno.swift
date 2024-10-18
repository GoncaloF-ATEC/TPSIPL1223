// classes e structs
/*
 
 Classe Pessoa: Crie uma classe que modele uma Aluno:

 Atributos: nome, idade, peso e altura
 Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
 
 
 */

class Aluno {
    
    var nome:String
    var email:String
    var idade: Int
    var altura: Float
    
    init(nome: String, email: String, idade: Int, altura: Float) {
        self.nome = nome
        self.email = email
        self.idade = idade
        self.altura = altura
    }
    
    
    func engordar(){
        
    }
    
    
    func crescer(x cm:Float = 0.5){
        self.altura += cm
        
    }
    func envelhecer(anos:Int = 1){
        idade += anos
        
        if idade > 21{
            return
        }
        
        crescer()
       
    }
}
