import { reactive } from 'vue'

export class User {
  login: string
  constructor() {
    this.login = ''
  }
}


export class Authentication {
  user: User | null = null
}

export const authentication = reactive(new Authentication())
