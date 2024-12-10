//
//  todo.swift
//  LoadApi
//
//  Created by Gonçalo Feliciano on 08/11/2024.
//

/*
 
 {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  }
  
 */


typealias ToDos = [Todo]


struct Todo: Identifiable, Codable{
    var userId: Int
    var id: Int
    var title: String
    var completed: Bool
}
