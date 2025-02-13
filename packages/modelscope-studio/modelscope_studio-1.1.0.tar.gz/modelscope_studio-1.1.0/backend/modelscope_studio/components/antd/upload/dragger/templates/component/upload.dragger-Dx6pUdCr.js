import { i as ve, a as z, r as ge, g as ye, w as T, b as be } from "./Index-DsTY7MQx.js";
const L = window.ms_globals.React, oe = window.ms_globals.React.useMemo, we = window.ms_globals.React.forwardRef, _e = window.ms_globals.React.useRef, he = window.ms_globals.React.useState, Ie = window.ms_globals.React.useEffect, q = window.ms_globals.ReactDOM.createPortal, xe = window.ms_globals.internalContext.useContextPropsContext, K = window.ms_globals.internalContext.ContextPropsProvider, Ee = window.ms_globals.antd.Upload;
var Re = /\s/;
function Se(e) {
  for (var t = e.length; t-- && Re.test(e.charAt(t)); )
    ;
  return t;
}
var Ce = /^\s+/;
function Le(e) {
  return e && e.slice(0, Se(e) + 1).replace(Ce, "");
}
var J = NaN, ke = /^[-+]0x[0-9a-f]+$/i, Ue = /^0b[01]+$/i, Fe = /^0o[0-7]+$/i, Oe = parseInt;
function X(e) {
  if (typeof e == "number")
    return e;
  if (ve(e))
    return J;
  if (z(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = z(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Le(e);
  var o = Ue.test(e);
  return o || Fe.test(e) ? Oe(e.slice(2), o ? 2 : 8) : ke.test(e) ? J : +e;
}
var A = function() {
  return ge.Date.now();
}, Te = "Expected a function", Pe = Math.max, je = Math.min;
function De(e, t, o) {
  var i, s, n, r, c, u, _ = 0, v = !1, l = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Te);
  t = X(t) || 0, z(o) && (v = !!o.leading, l = "maxWait" in o, n = l ? Pe(X(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function p(f) {
    var x = i, C = s;
    return i = s = void 0, _ = f, r = e.apply(C, x), r;
  }
  function h(f) {
    return _ = f, c = setTimeout(g, t), v ? p(f) : r;
  }
  function d(f) {
    var x = f - u, C = f - _, O = t - x;
    return l ? je(O, n - C) : O;
  }
  function I(f) {
    var x = f - u, C = f - _;
    return u === void 0 || x >= t || x < 0 || l && C >= n;
  }
  function g() {
    var f = A();
    if (I(f))
      return m(f);
    c = setTimeout(g, d(f));
  }
  function m(f) {
    return c = void 0, w && i ? p(f) : (i = s = void 0, r);
  }
  function R() {
    c !== void 0 && clearTimeout(c), _ = 0, i = u = s = c = void 0;
  }
  function a() {
    return c === void 0 ? r : m(A());
  }
  function S() {
    var f = A(), x = I(f);
    if (i = arguments, s = this, u = f, x) {
      if (c === void 0)
        return h(u);
      if (l)
        return clearTimeout(c), c = setTimeout(g, t), p(u);
    }
    return c === void 0 && (c = setTimeout(g, t)), r;
  }
  return S.cancel = R, S.flush = a, S;
}
var ie = {
  exports: {}
}, N = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ne = L, We = Symbol.for("react.element"), Ae = Symbol.for("react.fragment"), Me = Object.prototype.hasOwnProperty, qe = Ne.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ze = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function se(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Me.call(t, i) && !ze.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: We,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: qe.current
  };
}
N.Fragment = Ae;
N.jsx = se;
N.jsxs = se;
ie.exports = N;
var D = ie.exports;
const {
  SvelteComponent: Be,
  assign: Y,
  binding_callbacks: Q,
  check_outros: Ge,
  children: ce,
  claim_element: le,
  claim_space: He,
  component_subscribe: Z,
  compute_slots: Ke,
  create_slot: Je,
  detach: F,
  element: ae,
  empty: V,
  exclude_internal_props: $,
  get_all_dirty_from_scope: Xe,
  get_slot_changes: Ye,
  group_outros: Qe,
  init: Ze,
  insert_hydration: P,
  safe_not_equal: Ve,
  set_custom_element_data: de,
  space: $e,
  transition_in: j,
  transition_out: B,
  update_slot_base: et
} = window.__gradio__svelte__internal, {
  beforeUpdate: tt,
  getContext: nt,
  onDestroy: rt,
  setContext: ot
} = window.__gradio__svelte__internal;
function ee(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Je(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ae("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = le(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ce(t);
      s && s.l(r), r.forEach(F), this.h();
    },
    h() {
      de(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      P(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && et(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Ye(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Xe(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (j(s, n), o = !0);
    },
    o(n) {
      B(s, n), o = !1;
    },
    d(n) {
      n && F(t), s && s.d(n), e[9](null);
    }
  };
}
function it(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && ee(e)
  );
  return {
    c() {
      t = ae("react-portal-target"), o = $e(), n && n.c(), i = V(), this.h();
    },
    l(r) {
      t = le(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ce(t).forEach(F), o = He(r), n && n.l(r), i = V(), this.h();
    },
    h() {
      de(t, "class", "svelte-1rt0kpf");
    },
    m(r, c) {
      P(r, t, c), e[8](t), P(r, o, c), n && n.m(r, c), P(r, i, c), s = !0;
    },
    p(r, [c]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, c), c & /*$$slots*/
      16 && j(n, 1)) : (n = ee(r), n.c(), j(n, 1), n.m(i.parentNode, i)) : n && (Qe(), B(n, 1, 1, () => {
        n = null;
      }), Ge());
    },
    i(r) {
      s || (j(n), s = !0);
    },
    o(r) {
      B(n), s = !1;
    },
    d(r) {
      r && (F(t), F(o), F(i)), e[8](null), n && n.d(r);
    }
  };
}
function te(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function st(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const c = Ke(n);
  let {
    svelteInit: u
  } = t;
  const _ = T(te(t)), v = T();
  Z(e, v, (a) => o(0, i = a));
  const l = T();
  Z(e, l, (a) => o(1, s = a));
  const w = [], p = nt("$$ms-gr-react-wrapper"), {
    slotKey: h,
    slotIndex: d,
    subSlotIndex: I
  } = ye() || {}, g = u({
    parent: p,
    props: _,
    target: v,
    slot: l,
    slotKey: h,
    slotIndex: d,
    subSlotIndex: I,
    onDestroy(a) {
      w.push(a);
    }
  });
  ot("$$ms-gr-react-wrapper", g), tt(() => {
    _.set(te(t));
  }), rt(() => {
    w.forEach((a) => a());
  });
  function m(a) {
    Q[a ? "unshift" : "push"](() => {
      i = a, v.set(i);
    });
  }
  function R(a) {
    Q[a ? "unshift" : "push"](() => {
      s = a, l.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = Y(Y({}, t), $(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = $(t), [i, s, v, l, c, u, r, n, m, R];
}
class ct extends Be {
  constructor(t) {
    super(), Ze(this, t, st, it, Ve, {
      svelteInit: 5
    });
  }
}
const ne = window.ms_globals.rerender, M = window.ms_globals.tree;
function lt(e, t = {}) {
  function o(i) {
    const s = T(), n = new ct({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const c = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? M;
          return u.nodes = [...u.nodes, c], ne({
            createPortal: q,
            node: M
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== s), ne({
              createPortal: q,
              node: M
            });
          }), c;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
function at(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function dt(e, t = !1) {
  try {
    if (be(e))
      return e;
    if (t && !at(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function b(e, t) {
  return oe(() => dt(e, t), [e, t]);
}
const ut = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ft(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = pt(o, i), t;
  }, {}) : {};
}
function pt(e, t) {
  return typeof t == "number" && !ut.includes(e) ? t + "px" : t;
}
function G(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = L.Children.toArray(e._reactElement.props.children).map((n) => {
      if (L.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: c
        } = G(n.props.el);
        return L.cloneElement(n, {
          ...n.props,
          el: c,
          children: [...L.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(q(L.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: c,
      useCapture: u
    }) => {
      o.addEventListener(c, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: c
      } = G(n);
      t.push(...c), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function mt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const wt = we(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = _e(), [c, u] = he([]), {
    forceClone: _
  } = xe(), v = _ ? !0 : t;
  return Ie(() => {
    var h;
    if (!r.current || !e)
      return;
    let l = e;
    function w() {
      let d = l;
      if (l.tagName.toLowerCase() === "svelte-slot" && l.children.length === 1 && l.children[0] && (d = l.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), mt(n, d), o && d.classList.add(...o.split(" ")), i) {
        const I = ft(i);
        Object.keys(I).forEach((g) => {
          d.style[g] = I[g];
        });
      }
    }
    let p = null;
    if (v && window.MutationObserver) {
      let d = function() {
        var R, a, S;
        (R = r.current) != null && R.contains(l) && ((a = r.current) == null || a.removeChild(l));
        const {
          portals: g,
          clonedElement: m
        } = G(e);
        l = m, u(g), l.style.display = "contents", w(), (S = r.current) == null || S.appendChild(l);
      };
      d();
      const I = De(() => {
        d(), p == null || p.disconnect(), p == null || p.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      p = new window.MutationObserver(I), p.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      l.style.display = "contents", w(), (h = r.current) == null || h.appendChild(l);
    return () => {
      var d, I;
      l.style.display = "", (d = r.current) != null && d.contains(l) && ((I = r.current) == null || I.removeChild(l)), p == null || p.disconnect();
    };
  }, [e, v, o, i, n, s]), L.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...c);
});
function re(e, t) {
  return e ? /* @__PURE__ */ D.jsx(wt, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function U({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ D.jsx(K, {
    params: s,
    forceClone: !0,
    children: re(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ D.jsx(K, {
    params: s,
    forceClone: !0,
    children: re(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
function _t(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const It = lt(({
  slots: e,
  upload: t,
  showUploadList: o,
  progress: i,
  beforeUpload: s,
  customRequest: n,
  previewFile: r,
  isImageUrl: c,
  itemRender: u,
  iconRender: _,
  data: v,
  onChange: l,
  onValueChange: w,
  onRemove: p,
  fileList: h,
  setSlotParams: d,
  ...I
}) => {
  const g = e["showUploadList.downloadIcon"] || e["showUploadList.removeIcon"] || e["showUploadList.previewIcon"] || e["showUploadList.extra"] || typeof o == "object", m = _t(o), R = b(m.showPreviewIcon), a = b(m.showRemoveIcon), S = b(m.showDownloadIcon), f = b(s), x = b(n), C = b(i == null ? void 0 : i.format), O = b(r), ue = b(c), fe = b(u), pe = b(_), me = b(v), H = oe(() => (h == null ? void 0 : h.map((y) => ({
    ...y,
    name: y.orig_name || y.path,
    uid: y.url || y.path,
    status: "done"
  }))) || [], [h]);
  return /* @__PURE__ */ D.jsx(Ee.Dragger, {
    ...I,
    fileList: H,
    data: me || v,
    previewFile: O,
    isImageUrl: ue,
    itemRender: e.itemRender ? U({
      slots: e,
      setSlotParams: d,
      key: "itemRender"
    }) : fe,
    iconRender: e.iconRender ? U({
      slots: e,
      setSlotParams: d,
      key: "iconRender"
    }) : pe,
    onRemove: (y) => {
      p == null || p(y);
      const W = H.findIndex((E) => E.uid === y.uid), k = h.slice();
      k.splice(W, 1), w == null || w(k), l == null || l(k.map((E) => E.path));
    },
    beforeUpload: async (y, W) => {
      if (f && !await f(y, W))
        return !1;
      const k = (await t([y])).filter((E) => E);
      return w == null || w([...h, ...k]), l == null || l([...h.map((E) => E.path), ...k.map((E) => E.path)]), !1;
    },
    maxCount: 1,
    customRequest: x,
    progress: i && {
      ...i,
      format: C
    },
    showUploadList: g ? {
      ...m,
      showDownloadIcon: S || m.showDownloadIcon,
      showRemoveIcon: a || m.showRemoveIcon,
      showPreviewIcon: R || m.showPreviewIcon,
      downloadIcon: e["showUploadList.downloadIcon"] ? U({
        slots: e,
        setSlotParams: d,
        key: "showUploadList.downloadIcon"
      }) : m.downloadIcon,
      removeIcon: e["showUploadList.removeIcon"] ? U({
        slots: e,
        setSlotParams: d,
        key: "showUploadList.removeIcon"
      }) : m.removeIcon,
      previewIcon: e["showUploadList.previewIcon"] ? U({
        slots: e,
        setSlotParams: d,
        key: "showUploadList.previewIcon"
      }) : m.previewIcon,
      extra: e["showUploadList.extra"] ? U({
        slots: e,
        setSlotParams: d,
        key: "showUploadList.extra"
      }) : m.extra
    } : o
  });
});
export {
  It as UploadDragger,
  It as default
};
