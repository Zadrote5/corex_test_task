import {boot} from 'quasar/wrappers'
import { Store, store } from 'src/store/store';
import { Authentication, authentication } from 'src/store/authentication';


declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $repo: Store;
    $auth: Authentication
  }
}

export default boot(({ app }) => {
  // for use inside Vue files (Options API)
  app.config.globalProperties.$repo = store;
  app.config.globalProperties.$auth = authentication;
});

export { Store };
