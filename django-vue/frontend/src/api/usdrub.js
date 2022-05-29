import { HTTP } from './common'

export const usdru = {
  list () {
    return HTTP.get('/usdrub/').then(response => {
      return response.data
    })
  }
}

