//
//  btnView.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import SwiftUI

struct btnView: View {
    var txt:String
    var body: some View {
        Text(txt) // <p>Ola mundo</p>
            .frame(width: 120, height: 60)
            .fontWeight(.bold)
            .foregroundStyle(.blue)
            .background(.black)
            .clipShape(Capsule())
            .padding(8)
            .background(.gray)
            .clipShape(Capsule())
            .shadow(color: .red, radius: 17)
        
    }
}

#Preview {
    btnView(txt: "Ola Mundo")
}
