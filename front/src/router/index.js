import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomeView
		},
		{
			path: '/about',
			name: 'abaut',
			component: () => import('../views/AboutView.vue')
		},
		{
			path: '/write',
			name: 'Write Diary',
			component: () => import('../views/WriteView.vue')
		},
		{
			path: '/watch',
			name: 'Watch Diary Select',
			component: () => import('../views/WatchView.vue')
		},
		{
			path: '/watch/:day/:title',
			name: 'Watch Diary',
			component: () => import('../views/WatchDiary.vue')
		},
		{
			path: '/edit',
			name: 'Edit Diary Select',
			component: () => import('../views/EditView.vue')
		},
		{
			path: '/edit/:day/:title',
			name: 'Edit Diary',
			component: () => import('../views/EditDiary.vue')
		},
		{
			path: '/delete',
			name: 'Delete Diary',
			component: () => import('../views/DeleteDiary.vue')
		},
		{
			path: '/tree',
			name: 'Memory Tree',
			component: () => import('../views/TreeView.vue')
		}
	]
})

export default router
