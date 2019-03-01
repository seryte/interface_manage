<template>
  <div class="login-main-context">
    <div class="login-title">
      账号登录
      </div>
      <el-form ref="ruleForm" :model="form" :rules="rules" label-width="100px" class="login-ruleForm">
        <el-form-item label="用户名" prop="name">
          <el-input v-model="form.name"></el-input>
        </el-form-item>

          <el-form-item label="密码" prop="pwd">
          <el-input v-model="form.pwd"></el-input>
        </el-form-item>

      </el-form>
        <div class="login-button-class">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="warning" @click="register">注册</el-button>
        </div>
    </div>
  </template>
<script>
  import {login} from "../requests/user";

  export default {
    data() {
      return {
        form: {
          name: '',
          pwd: ''
        },
        rules: {
          name: [
            {required: true, message: '请输入用户名', trigger: 'blur'},
            {min: 3, max: 20, message: '长度3到20个字符', trigger: 'blur'}
          ],
          pwd: [
            {required: true, message: '请输入密码', trigger: 'blue'},
            {min: 3, max: 21, message: '长度3到21个字符', trigger: 'blue'}
          ],

        },
      }
    },
    methods: {
      login() {
        console.log('login!');
        this.$refs.ruleForm.validate((valid)=>{
          if(valid) {
            login(this.form.name, this.form.pwd).then(data=>{
              console.log(data)
            })
          }
          else{
            console.log("failed")
          }
        })
      },// login结束
      register(){
        console.log("register!")
        this.$refs.ruleForm.validate((valid)=>{
          if(valid) {
            alert("success")
          }
          else{
            console.log("failed")
          }
        })
      } // register结束
    } //methods结束
  }
</script>
<style scoped>
  .login-main-context {
    width: 400px;
    margin-left: auto;
    margin-right: auto;
    min-height: 100px;
    padding: 20px 30px 20px 5px;
    /*圆角*/
    border-radius: 5px;
    /*边框实线和颜色*/
    border: 1px solid #a0b1c4;
    margin-top: 50px;
  }

  .login-button-class {
    /*弹性布局*/
    display: flex;
    justify-content: space-between;
    padding-left: 25px;

  }

  .login-title {
    text-align: center;
  }

  .login-ruleForm {
    margin-top: 20px;
  }

</style>
