import {boot} from 'quasar/wrappers'
import { Store, store } from 'src/store/store';


declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $repo: Store;
  }
}

export default boot(({ app }) => {
  // for use inside Vue files (Options API)
  app.config.globalProperties.$repo = store;
});

export { Store };
