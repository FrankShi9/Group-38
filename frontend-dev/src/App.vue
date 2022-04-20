<template>
  <sidebar-menu
    v-model:collapsed="collapsed"
    :menu="menu"
    :theme="selectedTheme"
    :show-one-child="true"
    @update:collapsed="onToggleCollapse"
    @item-click="onItemClick"
  />
  <div
    v-if="isOnMobile && !collapsed"
    class="sidebar-overlay"
    @click="collapsed = true"
  />
  <div
    id="demo"
    :class="[{'collapsed' : collapsed}, {'onmobile' : isOnMobile}]"
  >
  <router-view />
  </div>
</template>

<script>
import { markRaw } from 'vue'
import cookies from 'vue-cookies'
import $ from 'jquery'

const separator = {
  template: '<hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px;">'
}

export default {
  name: 'App',
  data () {
    return {
      login_status: '',

      menu: [
        {
          header: 'Getting Started',
          hiddenOnCollapse: true
        },
        {
          href: '/home',
          title: 'Home',
          icon: 'fa fa-home'
        },
        {
          href: '/guidance',
          title: 'User Guidance',
          icon: 'fa fa-book'
        },
        
        {
          component: markRaw(separator)
        },

        {
          header: 'User Account',
          hiddenOnCollapse: true
        },
        {
          href: '/login',
          title: 'Login',
          icon: 'fa fa-sign-in-alt',
          hidden: false,
        },
        {
          href: '/history',
          title: 'History',
          icon: 'fa fa-history',
          hidden: true
        },
        {
          href: '/logout',
          title: 'Logout',
          icon: "fa fa-sign-out-alt",
          hidden: true
        },
        {
          component: markRaw(separator)
        },
        {
          href: '/AboutUs',
          title: 'About us',
          icon: 'fa fa-info'
        }

      ],
      collapsed: false,
      themes: [
        {
          name: 'Default theme',
          input: ''
        },
        {
          name: 'White theme',
          input: 'white-theme'
        }
      ],
      selectedTheme: 'white-theme',
      isOnMobile: false,
    }
  },

  mounted () {
    this.onResize()
    window.addEventListener('resize', this.onResize)
  },

  created() {
    this.isLogin()
  },

  methods: {
    isLogin() {
      // cookies.set('is_login', 'true')
      this.login_status = cookies.get('is_login');
      console.log('login status is ' + this.login_status)
      if (this.login_status == 'true') {
        this.menu[5].hidden = true;
        this.menu[6].hidden = false;
        this.menu[7].hidden = false;
      }
      else {
        // do nothing
        this.login_status = '';
      }
    },

    onToggleCollapse (collapsed) {
      console.log('onToggleCollapse')
    },
    onItemClick (event, item) {
      console.log('onItemClick')
      // console.log(event)
      // console.log(item)
    },
    onResize () {
      if (window.innerWidth <= 767) {
        this.isOnMobile = true
        this.collapsed = true
      } else {
        this.isOnMobile = false
        this.collapsed = false
      }
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600');

body,
html {
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 18px;
  background-color: #f2f4f7;
  color: #262626;
}

#demo {
  padding-left: 290px;
  transition: 0.3s ease;
}
#demo.collapsed {
  padding-left: 65px;
}
#demo.onmobile {
  padding-left: 65px;
}

.sidebar-overlay {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: #000;
  opacity: 0.5;
  z-index: 900;
}

.demo {
  padding: 50px;
}
</style>

