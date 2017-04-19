package com.core.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;
import java.io.*;
import java.util.Iterator;
import java.util.List;

/**
 * 跳转到婚纱管理页面的Controller
 * 
 * @author Administrator
 *
 */
@Controller
@RequestMapping("weddingDressCtr")
public class WeddingDressController extends BaseController {

	Logger log = Logger.getLogger(WeddingDressController.class);

	/*
	 * 跳转到婚纱管理页面，查看婚纱信息
	 */
	@RequestMapping(params = "index")
	public String index(HttpServletRequest request, HttpServletResponse response) {
		log.info("------------》跳转到婚纱管理页面，查看婚纱信息《------------");

		return "wedding_dress/wedding_dress_list";
	}

	/*
	 * 添加婚纱
	 */
	@RequestMapping(params = "addWedding")
	public String addWedding(HttpServletRequest request, HttpServletResponse response) {
		log.info("------------》添加婚纱《------------");

		return "wedding_dress/wedding_dress_add";
	}

	/*
	 * 添加套餐
	 */
	@RequestMapping(params = "addPackage")
	public String addPackage(HttpServletRequest request, HttpServletResponse response) {
		log.info("------------》添加套餐《------------");

		return "wedding_dress/wedding_package_add";
	}

	/*
	 * 套餐管理
	 */
	@RequestMapping(params = "indexPackage")
	public String indexPackage(HttpServletRequest request, HttpServletResponse response) {
		log.info("------------》套餐管理《------------");

		return "wedding_dress/wedding_package_list";
	}

	@RequestMapping(value = "/savePicture.do")
	public void test(HttpServletRequest request, HttpServletResponse response) {
		final long MAX_SIZE = 3 * 1024 * 1024;// 设置上传文件最大为 3M
		// 允许上传的文件格式
		final String[] allowedExt = new String[] { "jpg", "jpeg", "gif", "txt",
				"doc", "docx", "mp3", "wma", "m4a" };
		response.setContentType("text/html");
		// 设置字符编码为UTF-8, 这样支持汉字显示
		response.setCharacterEncoding("UTF-8");

		// 实例化一个硬盘文件工厂,用来配置上传组件ServletFileUpload
		DiskFileItemFactory dfif = new DiskFileItemFactory();
		String pathname = (request.getSession().getServletContext().getRealPath("/") + "ImagesUploadTemp");
		dfif.setRepository(new File(pathname));// 设置存放临时文件的目录,web根目录下的ImagesUploadTemp目录

		// 用以上工厂实例化上传组件
		ServletFileUpload sfu = new ServletFileUpload(dfif);
		// 设置最大上传尺寸
		sfu.setSizeMax(MAX_SIZE);

		PrintWriter out = null;
		try {
			out = response.getWriter();
		} catch (IOException e) {
			e.printStackTrace();
		}
		// 从request得到 所有 上传域的列表
		List fileList = null;
		try {
			fileList = sfu.parseRequest(request);
		} catch (FileUploadException e) {   // 处理文件尺寸过大异常
			if (e instanceof Exception) {
				System.err.println("图片大小错误!");
				return;
			}
			e.printStackTrace();
		}
		// 没有文件上传
		if (fileList == null || fileList.size() == 0) {
			System.err.println("没有文件!");
			return;
		}
		// 得到所有上传的文件
		Iterator fileItr = fileList.iterator();
		// 循环处理所有文件
		while (fileItr.hasNext()) {
			FileItem fileItem = null;
			String path = null;
			long size = 0;
			// 得到当前文件
			fileItem = (FileItem) fileItr.next();
			// 忽略简单form字段而不是上传域的文件域(<input type="text" />等)
			if (fileItem == null || fileItem.isFormField()) {
				continue;
			}
			// 得到文件的完整路径
			path = fileItem.getName();
			// 得到文件的大小
			size = fileItem.getSize();
			if ("".equals(path) || size == 0) {
				System.err.println("没有文件!");
				return;
			}
			// 得到去除路径的文件名
			String t_name = path.substring(path.lastIndexOf("\\") + 1);
			// 得到文件的扩展名
			String t_ext = t_name.substring(t_name.lastIndexOf(".") + 1);
			// 限制文件格式
			int allowFlag = 0;
			int allowedExtCount = allowedExt.length;
			for (; allowFlag < allowedExtCount; allowFlag++) {
				if (allowedExt[allowFlag].equals(t_ext))
					break;
			}
			if (allowFlag == allowedExtCount) {
				System.err.println("文件格式错误!");
				return;
			}

			long now = System.currentTimeMillis();
			// 根据系统时间生成上传后保存的文件名
			String prefix = String.valueOf(now);
			// 保存的最终文件完整路径
			String u_name = request.getSession().getServletContext().getRealPath("/") + "ImagesUploaded/" + prefix + "." + t_ext;
			try {
				// 保存文件
				fileItem.write(new File(u_name));
				System.err.println("图片保存成功!");
			} catch (Exception e) {
				// e.printStackTrace();
				System.err.println("图片保存失败! error : =====" + e);
			}

		}
	}

}
