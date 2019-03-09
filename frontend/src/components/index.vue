<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

  </div>
</template>

<script>
  import {get_user} from "../requests/user";

  export default {
    name: 'HelloWorld',
    data() {
      return {
        current_user: {},
        msg: 'Hello Welcome to Your Vue.js App'
      }
    },
    mounted() {
      get_user().then(data => {
        if (true === data.success) {
          console.log(data.data)
          this.current_user = data.data
        } else {
          this.$message.error(data.message)  // 弹出后台message中的信息
          this.$router.push('/login');
        }
      })
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
