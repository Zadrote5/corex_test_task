import { reactive } from 'vue'
import axios, { AxiosResponse } from 'axios'
export type UserRaw = {
  username: string
  [key: string]: any
}

export class User {
  username: string
  constructor(data: UserRaw) {
    this.username = data.username
  }
}
export type auth_token = {
  auth_token: string
}


export class Authentication {
  user: User | null = null

  async me(): Promise<void> {
    try {
      const token = localStorage.getItem('token')
      console.log(token)
      const responseCheck: AxiosResponse<UserRaw> = await axios({
        method: 'GET',
        url: 'http://0.0.0.0:8000/auth/users/me/',
        headers: {
          Authorization: `Token ${token || ''}`
        }
      })
      console.log(responseCheck)
      authentication.user = new User(responseCheck.data)
    } catch (e) {
      console.log(e)
    }
  }

  async login(login: string, pass: string): Promise<void> {
    const responseAuth: AxiosResponse<auth_token> = await axios({
      method: 'post',
      url: 'http://0.0.0.0:8000/auth/token/login',
      data: {
        'username': login,
        'password': pass
      }
    })
    if (responseAuth.data['auth_token']) {
      localStorage.setItem('token', responseAuth.data['auth_token'])
      await this.me()
    }
  }
}

export const authentication = reactive(new Authentication())
