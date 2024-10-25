//
//  demoView.swift
//  aula_5_demoUI
//
//  Created by Gonçalo Feliciano on 25/10/2024.
//

import SwiftUI

struct demoView: View {
    @State var red: Double = 1
    
    var body: some View {
        VStack{
            Rectangle()
                .frame(width: 120, height: 350)
                .foregroundStyle(Color(red: red, green: 0.5, blue: 0.5, opacity: 1))
            
                
            Slider(value: $red, in: 0...1, step: 0.001)
            
            
            
        }
    }
}

#Preview {
    demoView()
}
