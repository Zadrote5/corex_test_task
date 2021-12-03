import {reactive} from 'vue'


export class Store {
  drawer = false
  dialog = false
  item = {
    id: 1
  }

  authorList: Array<Author> = []
  countryList: Array<Country> = []
  cityList: Array<City> = []
  newsList: Array<News> = []
  newsItem: News | null = null
  authorItem: Author | null = null
}
export type AuthorRaw = {
  id?: number
  name?: string
  email?: string
}
export class Author {
  name?: string
  id?: number
  email?: string
  constructor(data: AuthorRaw) {
    this.id = data.id
    this.name = data.name
    if (data.email)
      this.email =data.email
  }

}
export type CountryRaw = {
  id: number
  name: string
}
export class Country {
  id: number
  name: string
  constructor(data: CountryRaw) {
    this.id = data.id
    this.name = data.name
  }
}
export type CityRaw = {
  id: number
  name: string
  country: Country
}

export class City {
  id: number
  name: string
  country: Country
  constructor(data: CityRaw) {
    this.id = data.id
    this.name = data.name
    this.country = data.country
  }
}

export type NewsRaw = {
  id?: number
  title?: string,
  cities?: Array<CityRaw>
  author?: Author
  content?: string
  is_published?: boolean
}

export class News {
  id: number
  title?: string;
  author?: Author | null
  content?: string
  is_published?: boolean
  cities?: Array<City>
  constructor(data: NewsRaw) {
    if (data.id) {
      this.id = data.id
    }
    else {
      this.id = 0
    }
    this.title = data.title
    if (data.cities)
      this.cities = data.cities.map(val => new City(val))
    if (data.author) {
      this.author = data.author
    }
    if (data.content)
      this.content = data.content
    if (data.is_published)
      this.is_published = data.is_published
  }

  toJson() {

    return {
      'title': this.title,
      'content': this.content,
      'is_published': this.is_published,
      'author': this.author?.id,
      'cities': this.cities?.map((val: City) => val.id),
    }
  }

}

export const store = reactive(new Store())
