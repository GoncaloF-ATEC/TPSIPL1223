//
//  newView.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import SwiftUI

struct newView: View {
    
    var nome:String
    @Binding var num:Int
    
    var body: some View {
        VStack{
            Text("\(nome) - \(num)")
            
            
            Stepper("Mudar Valor", value: $num, in: 0...100, step: 4)
                .frame(width: 100)
        
        }
        .navigationTitle("Pagina de infos - \(num)")
    }
}

#Preview {
    newView(nome: "Gonçalo", num: .constant(0))
}
