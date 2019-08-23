'use strict';

var gulp = require( 'gulp' );
var sass = require( 'gulp-sass' );
var uglifycss = require( 'gulp-uglifycss' );
var minify = require('gulp-minify');
var imagemin = require('gulp-imagemin');

sass.compiler = require('node-sass');

gulp.task('dependencies', function(done) {        
    gulp.src('./node_modules/jquery/dist/jquery.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/jquery/'));
    
    gulp.src('./node_modules/popper.js/dist/umd/popper.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/bootstrap/'));
    
    gulp.src('./node_modules/bootstrap/dist/js/bootstrap.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/bootstrap/'));
        
    gulp.src('./node_modules/chosen-js/chosen.jquery.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/chosen-js/'));
    
    gulp.src('./node_modules/bootstrap4c-chosen/dist/css/component-chosen.css')
        .pipe(gulp.dest('./static/dist/vendors/css/bootstrap4c/'));
    
    gulp.src('./node_modules/overlayscrollbars/js/OverlayScrollbars.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/overlayscrollbars/'));
    
    gulp.src('./node_modules/overlayscrollbars/css/OverlayScrollbars.min.css')
        .pipe(gulp.dest('./static/dist/vendors/css/overlayscrollbars/'));
    
    gulp.src('./node_modules/toastr/build/toastr.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/toastr/'));
    
    gulp.src('./node_modules/toastr/build/toastr.min.css')
        .pipe(gulp.dest('./static/dist/vendors/css/toastr/'));
    
    gulp.src('./node_modules/magnific-popup/dist/jquery.magnific-popup.min.js')
        .pipe(gulp.dest('./static/dist/vendors/js/magnific-popup'));
    
    gulp.src('./node_modules/magnific-popup/dist/magnific-popup.css')
        .pipe(gulp.dest('./static/dist/vendors/css/magnific-popup'));

    done();
});

gulp.task('sass', function() {
    return gulp.src('./static/scss/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('./static/css'));
});

gulp.task('uglify', function(done) {
    gulp.src('./static/css/*.css')
        .pipe(uglifycss({
            'uglyComments': true,
        }))
        .pipe(gulp.dest('./static/dist/css/'));

    done();
});

gulp.task('minify', function(done) {
    gulp.src('./static/js/*.js')
        .pipe(minify({
            ext: {
                min: '.min.js',
            }
        }))
        .pipe(gulp.dest('./static/dist/js/'));

    done();
});

gulp.task('imagemin', function(done) {
    gulp.src('./static/img/*')
        .pipe(imagemin())
        .pipe(gulp.dest('./static/dist/img/'));

    done();
});

gulp.task('run', gulp.series('sass', 'uglify', 'minify', 'imagemin'));

gulp.task('watch', function() {
    gulp.watch('./static/scss/*.scss', gulp.series('sass'));
    gulp.watch('./static/css/*.css', gulp.series('uglify'));
});

gulp.task('default', gulp.series('run', 'watch'));