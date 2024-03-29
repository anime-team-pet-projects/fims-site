import type { AxiosRequestConfig } from 'axios'
import { AxiosService } from '@/api/axiosService'

class UsersApi extends AxiosService {
  constructor(config?: AxiosRequestConfig) {
    super(config)
  }

  async userRegister(payload: any) {
    return this.axiosCall<any>({
      method: 'post',
      url: '/auth/users/',
      data: payload,
    })
  }

  async userAuthorization(payload: any) {
    return this.axiosCall<any>({
      method: 'post',
      url: '/auth/jwt/create/',
      data: payload,
    })
  }
}

export default new UsersApi({
  baseURL: 'http://localhost:8000',
  withCredentials: false,
})
