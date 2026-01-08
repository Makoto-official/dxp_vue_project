<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'

// 数据状态
const movies_data = ref([])
const id = ref('')
const title = ref('')
const rank = ref('')
const loading = ref(false)
const isEditing = ref(false)
const showModal = ref(false)
const searchQuery = ref('')

// 通知消息
const notification = ref({
  show: false,
  message: '',
  type: 'success' // success, error, warning, info
})

// API基础URL
const API_BASE = 'http://127.0.0.1:8000/douban'

// 显示通知
const showNotification = (message, type = 'success') => {
  notification.value = { show: true, message, type }
  setTimeout(() => {
    notification.value.show = false
  }, 3000)
}

// 获取电影列表
const get_movies = async () => {
  loading.value = true
  try {
    const response = await axios.get(`${API_BASE}/get_movies`)
    movies_data.value = response.data
    showNotification('电影列表加载成功', 'success')
  } catch (error) {
    console.error(error)
    showNotification('加载电影列表失败: ' + (error.response?.data || error.message), 'error')
  } finally {
    loading.value = false
  }
}

// 删除电影（带确认）
const delete_movie = async (p_id, movieTitle) => {
  if (!confirm(`确定要删除电影《${movieTitle}》吗？此操作不可恢复！`)) {
    return
  }
  
  loading.value = true
  try {
    await axios.get(`${API_BASE}/delete_movie?id=${p_id}`)
    await get_movies()
    showNotification('电影删除成功', 'success')
  } catch (error) {
    console.error(error)
    showNotification('删除失败: ' + (error.response?.data || error.message), 'error')
  } finally {
    loading.value = false
  }
}

// 添加或更新电影
const add_update_movie = async () => {
  // 表单验证
  if (!title.value.trim()) {
    showNotification('请输入电影名称', 'warning')
    return
  }
  if (!rank.value || isNaN(rank.value)) {
    showNotification('请输入有效的排名数字', 'warning')
    return
  }

  loading.value = true
  const data = new FormData()
  data.append('title', title.value.trim())
  data.append('rank', rank.value)
  
  try {
    if (isEditing.value && id.value) {
      // 更新电影
      data.append('id', id.value)
      await axios.post(`${API_BASE}/update_movie`, data)
      showNotification('电影更新成功', 'success')
    } else {
      // 添加新电影
      await axios.post(`${API_BASE}/add_movie`, data)
      showNotification('电影添加成功', 'success')
    }
    
    await get_movies()
    resetForm()
    showModal.value = false
  } catch (error) {
    console.error(error)
    showNotification(
      (isEditing.value ? '更新' : '添加') + '失败: ' + (error.response?.data || error.message),
      'error'
    )
  } finally {
    loading.value = false
  }
}

// 编辑电影
const edit_movie = (movie) => {
  isEditing.value = true
  id.value = movie.id
  title.value = movie.title
  rank.value = movie.rank
  showModal.value = true
}

// 新增电影
const add_new_movie = () => {
  resetForm()
  isEditing.value = false
  showModal.value = true
}

// 重置表单
const resetForm = () => {
  id.value = ''
  title.value = ''
  rank.value = ''
  isEditing.value = false
}

// 关闭模态框
const closeModal = () => {
  showModal.value = false
  resetForm()
}

// 过滤电影（搜索功能）
const filteredMovies = ref([])
const filterMovies = () => {
  if (!searchQuery.value.trim()) {
    filteredMovies.value = movies_data.value
  } else {
    const query = searchQuery.value.toLowerCase()
    filteredMovies.value = movies_data.value.filter(movie =>
      movie.title.toLowerCase().includes(query) ||
      movie.id.toString().includes(query)
    )
  }
}

// 监听搜索和电影数据变化
const updateFilteredMovies = () => {
  filterMovies()
}

// 页面加载时获取数据
onMounted(() => {
  get_movies()
})

// 监听电影数据和搜索查询的变化
import { watch } from 'vue'
watch([movies_data, searchQuery], updateFilteredMovies, { immediate: true })

</script>

<template>
  <div class="movie-manager">
    <!-- 通知组件 -->
    <transition name="notification">
      <div v-if="notification.show" :class="['notification', notification.type]">
        <span class="notification-icon">
          {{ notification.type === 'success' ? '✓' : notification.type === 'error' ? '✕' : notification.type === 'warning' ? '⚠' : 'ℹ' }}
        </span>
        <span>{{ notification.message }}</span>
      </div>
    </transition>

    <!-- 加载遮罩 -->
    <div v-if="loading" class="loading-overlay">
      <div class="spinner"></div>
    </div>

    <!-- 头部 -->
    <header class="header">
      <h1 class="title">
        <span class="icon">🎬</span>
        电影管理系统
      </h1>
      <p class="subtitle">轻松管理您的电影收藏</p>
    </header>

    <!-- 操作栏 -->
    <div class="toolbar">
      <div class="search-box">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="搜索电影名称或ID..."
          class="search-input"
        />
        <span class="search-icon">🔍</span>
      </div>
      <div class="toolbar-buttons">
        <button @click="get_movies" class="btn btn-refresh" :disabled="loading">
          <span class="btn-icon">🔄</span>
          刷新列表
        </button>
        <button @click="add_new_movie" class="btn btn-primary">
          <span class="btn-icon">➕</span>
          添加电影
        </button>
      </div>
    </div>

    <!-- 电影表格 -->
    <div class="table-container">
      <table class="movie-table" v-if="filteredMovies.length > 0">
        <thead>
          <tr>
            <th>ID</th>
            <th>电影名称</th>
            <th>排名</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="movie in filteredMovies" :key="movie.id" class="movie-row">
            <td class="movie-id">{{ movie.id }}</td>
            <td class="movie-title">{{ movie.title }}</td>
            <td class="movie-rank">
              <span class="rank-badge">{{ movie.rank }}</span>
            </td>
            <td class="movie-actions">
              <button @click="edit_movie(movie)" class="btn-action btn-edit" title="编辑">
                <span>✏️</span>
              </button>
              <button @click="delete_movie(movie.id, movie.title)" class="btn-action btn-delete" title="删除">
                <span>🗑️</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <!-- 空状态 -->
      <div v-else class="empty-state">
        <div class="empty-icon">📽️</div>
        <p class="empty-text">{{ searchQuery ? '未找到匹配的电影' : '暂无电影数据' }}</p>
        <button v-if="!searchQuery" @click="add_new_movie" class="btn btn-primary">
          添加第一部电影
        </button>
      </div>
    </div>

    <!-- 统计信息 -->
    <div class="stats" v-if="movies_data.length > 0">
      <p>共 <strong>{{ movies_data.length }}</strong> 部电影</p>
      <p v-if="searchQuery">显示 <strong>{{ filteredMovies.length }}</strong> 个搜索结果</p>
    </div>

    <!-- 添加/编辑模态框 -->
    <transition name="modal">
      <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
        <div class="modal">
          <div class="modal-header">
            <h2>{{ isEditing ? '编辑电影' : '添加新电影' }}</h2>
            <button @click="closeModal" class="modal-close">&times;</button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="add_update_movie">
              <div class="form-group" v-if="isEditing">
                <label>ID</label>
                <input type="text" v-model="id" readonly class="form-input" />
              </div>
              <div class="form-group">
                <label>电影名称 <span class="required">*</span></label>
                <input
                  type="text"
                  v-model="title"
                  placeholder="请输入电影名称"
                  class="form-input"
                  required
                />
              </div>
              <div class="form-group">
                <label>排名 <span class="required">*</span></label>
                <input
                  type="number"
                  v-model="rank"
                  placeholder="请输入排名"
                  class="form-input"
                  required
                  min="1"
                />
              </div>
              <div class="modal-footer">
                <button type="button" @click="closeModal" class="btn btn-secondary">
                  取消
                </button>
                <button type="submit" class="btn btn-primary" :disabled="loading">
                  {{ isEditing ? '更新' : '添加' }}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<style scoped>
/* 主容器 */
.movie-manager {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

/* 通知样式 */
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 16px 24px;
  border-radius: 8px;
  background: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 1000;
  min-width: 300px;
  font-weight: 500;
}

.notification-icon {
  font-size: 20px;
  font-weight: bold;
}

.notification.success {
  border-left: 4px solid #10b981;
  color: #065f46;
}

.notification.error {
  border-left: 4px solid #ef4444;
  color: #991b1b;
}

.notification.warning {
  border-left: 4px solid #f59e0b;
  color: #92400e;
}

.notification.info {
  border-left: 4px solid #3b82f6;
  color: #1e40af;
}

.notification-enter-active,
.notification-leave-active {
  transition: all 0.3s ease;
}

.notification-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.notification-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

/* 加载遮罩 */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 头部 */
.header {
  text-align: center;
  margin-bottom: 40px;
  color: #1e293b;
}

.title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
}

.icon {
  font-size: 52px;
}

.subtitle {
  font-size: 18px;
  opacity: 0.9;
}

/* 工具栏 */
.toolbar {
  background: white;
  padding: 24px;
  border-radius: 12px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  gap: 32px;
  align-items: center;
  flex-wrap: wrap;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.search-box {
  position: relative;
  width: 400px;
  max-width: 100%;
  min-width: 0; /* 允许 flex 子项 在窄屏下收缩，防止溢出 */
}

.search-input {
  width: 100%;
  padding: 12px 40px 12px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 16px;
  transition: all 0.3s;
  box-sizing: border-box; /* 将 padding 包含在宽度内，避免溢出 */
  max-width: 100%;
  min-width: 0;
}

.search-input:focus {
  outline: none;
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 18px;
  pointer-events: none;
}

.toolbar-buttons {
  display: flex;
  gap: 24px;
}

/* 按钮样式 */
.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-primary {
  background: #6366f1;
  color: white;
  box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.1), 0 2px 4px -1px rgba(99, 102, 241, 0.06);
}

.btn-primary:hover:not(:disabled) {
  background: #4f46e5;
  transform: translateY(-1px);
  box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.15), 0 4px 6px -2px rgba(99, 102, 241, 0.1);
}

.btn-refresh {
  background: #f3f4f6;
  color: #374151;
}

.btn-refresh:hover:not(:disabled) {
  background: #e5e7eb;
}

.btn-secondary {
  background: #6b7280;
  color: white;
}

.btn-secondary:hover {
  background: #4b5563;
}

.btn-icon {
  font-size: 18px;
}

/* 表格容器 */
.table-container {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 24px;
}

/* 表格 */
.movie-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed; /* 固定列宽，确保表头和列对齐 */
  white-space: nowrap; /* 优先不换行，便于对齐 */
}

.movie-table th,
.movie-table td {
  vertical-align: middle; /* 垂直居中 */
  box-sizing: border-box;
}

/* 指定列宽，防止不规则换行导致表头与列错位 */
.movie-table th:nth-child(1),
.movie-table td:nth-child(1) {
  width: 10%;
  text-align: center;
}

.movie-table th:nth-child(2),
.movie-table td:nth-child(2) {
  width: 60%;
  text-align: left;
}

.movie-table th:nth-child(3),
.movie-table td:nth-child(3) {
  width: 15%;
  text-align: center;
}

.movie-table th:nth-child(4),
.movie-table td:nth-child(4) {
  width: 15%;
  text-align: center;
}

.movie-table thead {
  background: #f1f5f9;
  color: #475569;
}

.movie-table th {
  padding: 16px;
  text-align: left;
  font-weight: 600;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-bottom: 1px solid #e2e8f0;
}

.movie-table tbody tr {
  border-bottom: 1px solid #e5e7eb;
  transition: background 0.2s;
}

.movie-table tbody tr:hover {
  background: #f9fafb;
}

.movie-table tbody tr:last-child {
  border-bottom: none;
}

.movie-table td {
  padding: 16px;
}

.movie-id {
  color: #6b7280;
  font-weight: 500;
  font-family: monospace;
}

.movie-title {
  font-weight: 600;
  color: #111827;
  font-size: 16px;
  display: block;
  overflow: hidden;
  text-overflow: ellipsis; /* 长文本省略 */
  white-space: nowrap;
}

.movie-rank {
  text-align: center;
}

.rank-badge {
  display: inline-block;
  padding: 4px 12px;
  background: #e0e7ff;
  color: #4338ca;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 14px;
}

/* 操作按钮 */
.movie-actions {
  display: flex;
  gap: 8px;
}

.btn-action {
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 16px;
}

.btn-edit {
  background: #dbeafe;
  color: #1e40af;
}

.btn-edit:hover {
  background: #3b82f6;
  transform: scale(1.1);
}

.btn-delete {
  background: #fee2e2;
  color: #991b1b;
}

.btn-delete:hover {
  background: #ef4444;
  transform: scale(1.1);
}

/* 空状态 */
.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 80px;
  margin-bottom: 20px;
  opacity: 0.5;
}

.empty-text {
  font-size: 18px;
  color: #6b7280;
  margin-bottom: 24px;
}

/* 统计信息 */
.stats {
  background: white;
  padding: 16px 24px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  gap: 24px;
  justify-content: center;
  color: #6b7280;
}

.stats strong {
  color: #6366f1;
  font-size: 18px;
}

/* 模态框 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal {
  background: white;
  border-radius: 16px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.modal-header {
  padding: 24px;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h2 {
  font-size: 24px;
  color: #111827;
  margin: 0;
}

.modal-close {
  background: none;
  border: none;
  font-size: 32px;
  color: #6b7280;
  cursor: pointer;
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all 0.2s;
}

.modal-close:hover {
  background: #f3f4f6;
  color: #111827;
}

.modal-body {
  padding: 24px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  font-weight: 500;
  color: #475569;
  font-size: 14px;
}

.required {
  color: #ef4444;
}

.form-input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 14px;
  transition: all 0.2s;
  box-sizing: border-box;
  background-color: #f8fafc;
}

.form-input:focus {
  outline: none;
  border-color: #6366f1;
  background-color: #ffffff;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1);
}

.form-input:read-only {
  background: #f3f4f6;
  color: #6b7280;
}

.modal-footer {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
  margin-top: 24px;
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .modal,
.modal-leave-active .modal {
  transition: transform 0.3s;
}

.modal-enter-from .modal,
.modal-leave-to .modal {
  transform: scale(0.9);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .title {
    font-size: 32px;
  }
  
  .toolbar {
    flex-direction: column;
    align-items: stretch;
    padding: 16px; /* 缩小内边距，避免在小屏下溢出 */
  }
  
  .search-box {
    width: 100%;
  }
  
  .toolbar-buttons {
    width: 100%;
    flex-direction: column;
  }
  
  .toolbar-buttons .btn {
    width: 100%;
    justify-content: center;
    white-space: normal; /* 允许按钮文本换行，防止导致溢出 */
  }
  
  .movie-table {
    font-size: 14px;
    /* 窄屏下允许自动布局和换行，避免页面横向溢出 */
    table-layout: auto;
    white-space: normal;
  }
  
  .movie-table th,
  .movie-table td {
    padding: 12px 8px;
  }

  .movie-title {
    white-space: normal;
    overflow: visible;
    text-overflow: unset;
  }
  
  .stats {
    flex-direction: column;
    gap: 8px;
    text-align: center;
  }
}
</style>