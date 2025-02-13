import { i as fe, a as M, r as me, g as he, w as j, b as _e } from "./Index-CsTvX5ur.js";
const R = window.ms_globals.React, ce = window.ms_globals.React.forwardRef, ae = window.ms_globals.React.useRef, ue = window.ms_globals.React.useState, de = window.ms_globals.React.useEffect, ee = window.ms_globals.React.useMemo, D = window.ms_globals.ReactDOM.createPortal, ge = window.ms_globals.internalContext.useContextPropsContext, L = window.ms_globals.internalContext.ContextPropsProvider, pe = window.ms_globals.antd.TreeSelect, we = window.ms_globals.createItemsContext.createItemsContext;
var xe = /\s/;
function be(e) {
  for (var t = e.length; t-- && xe.test(e.charAt(t)); )
    ;
  return t;
}
var Ce = /^\s+/;
function ye(e) {
  return e && e.slice(0, be(e) + 1).replace(Ce, "");
}
var z = NaN, Ie = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Re = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (fe(e))
    return z;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ye(e);
  var o = Ee.test(e);
  return o || ve.test(e) ? Re(e.slice(2), o ? 2 : 8) : Ie.test(e) ? z : +e;
}
var W = function() {
  return me.Date.now();
}, Te = "Expected a function", ke = Math.max, Se = Math.min;
function Oe(e, t, o) {
  var i, l, n, r, s, a, x = 0, p = !1, c = !1, m = !0;
  if (typeof e != "function")
    throw new TypeError(Te);
  t = G(t) || 0, M(o) && (p = !!o.leading, c = "maxWait" in o, n = c ? ke(G(o.maxWait) || 0, t) : n, m = "trailing" in o ? !!o.trailing : m);
  function d(g) {
    var y = i, v = l;
    return i = l = void 0, x = g, r = e.apply(v, y), r;
  }
  function w(g) {
    return x = g, s = setTimeout(_, t), p ? d(g) : r;
  }
  function f(g) {
    var y = g - a, v = g - x, H = t - y;
    return c ? Se(H, n - v) : H;
  }
  function h(g) {
    var y = g - a, v = g - x;
    return a === void 0 || y >= t || y < 0 || c && v >= n;
  }
  function _() {
    var g = W();
    if (h(g))
      return C(g);
    s = setTimeout(_, f(g));
  }
  function C(g) {
    return s = void 0, m && i ? d(g) : (i = l = void 0, r);
  }
  function I() {
    s !== void 0 && clearTimeout(s), x = 0, i = a = l = s = void 0;
  }
  function u() {
    return s === void 0 ? r : C(W());
  }
  function E() {
    var g = W(), y = h(g);
    if (i = arguments, l = this, a = g, y) {
      if (s === void 0)
        return w(a);
      if (c)
        return clearTimeout(s), s = setTimeout(_, t), d(a);
    }
    return s === void 0 && (s = setTimeout(_, t)), r;
  }
  return E.cancel = I, E.flush = u, E;
}
var te = {
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
var je = R, Pe = Symbol.for("react.element"), Fe = Symbol.for("react.fragment"), Le = Object.prototype.hasOwnProperty, Ne = je.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, We = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ne(e, t, o) {
  var i, l = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Le.call(t, i) && !We.hasOwnProperty(i) && (l[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) l[i] === void 0 && (l[i] = t[i]);
  return {
    $$typeof: Pe,
    type: e,
    key: n,
    ref: r,
    props: l,
    _owner: Ne.current
  };
}
N.Fragment = Fe;
N.jsx = ne;
N.jsxs = ne;
te.exports = N;
var b = te.exports;
const {
  SvelteComponent: Ae,
  assign: q,
  binding_callbacks: V,
  check_outros: De,
  children: re,
  claim_element: oe,
  claim_space: Me,
  component_subscribe: J,
  compute_slots: Ue,
  create_slot: Be,
  detach: k,
  element: le,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: He,
  get_slot_changes: ze,
  group_outros: Ge,
  init: qe,
  insert_hydration: P,
  safe_not_equal: Ve,
  set_custom_element_data: ie,
  space: Je,
  transition_in: F,
  transition_out: U,
  update_slot_base: Xe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ye,
  getContext: Ke,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function K(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), l = Be(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = le("svelte-slot"), l && l.c(), this.h();
    },
    l(n) {
      t = oe(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = re(t);
      l && l.l(r), r.forEach(k), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      P(n, t, r), l && l.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      l && l.p && (!o || r & /*$$scope*/
      64) && Xe(
        l,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? ze(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : He(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (F(l, n), o = !0);
    },
    o(n) {
      U(l, n), o = !1;
    },
    d(n) {
      n && k(t), l && l.d(n), e[9](null);
    }
  };
}
function $e(e) {
  let t, o, i, l, n = (
    /*$$slots*/
    e[4].default && K(e)
  );
  return {
    c() {
      t = le("react-portal-target"), o = Je(), n && n.c(), i = X(), this.h();
    },
    l(r) {
      t = oe(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), re(t).forEach(k), o = Me(r), n && n.l(r), i = X(), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(r, s) {
      P(r, t, s), e[8](t), P(r, o, s), n && n.m(r, s), P(r, i, s), l = !0;
    },
    p(r, [s]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, s), s & /*$$slots*/
      16 && F(n, 1)) : (n = K(r), n.c(), F(n, 1), n.m(i.parentNode, i)) : n && (Ge(), U(n, 1, 1, () => {
        n = null;
      }), De());
    },
    i(r) {
      l || (F(n), l = !0);
    },
    o(r) {
      U(n), l = !1;
    },
    d(r) {
      r && (k(t), k(o), k(i)), e[8](null), n && n.d(r);
    }
  };
}
function Q(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function et(e, t, o) {
  let i, l, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const s = Ue(n);
  let {
    svelteInit: a
  } = t;
  const x = j(Q(t)), p = j();
  J(e, p, (u) => o(0, i = u));
  const c = j();
  J(e, c, (u) => o(1, l = u));
  const m = [], d = Ke("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: h
  } = he() || {}, _ = a({
    parent: d,
    props: x,
    target: p,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(u) {
      m.push(u);
    }
  });
  Ze("$$ms-gr-react-wrapper", _), Ye(() => {
    x.set(Q(t));
  }), Qe(() => {
    m.forEach((u) => u());
  });
  function C(u) {
    V[u ? "unshift" : "push"](() => {
      i = u, p.set(i);
    });
  }
  function I(u) {
    V[u ? "unshift" : "push"](() => {
      l = u, c.set(l);
    });
  }
  return e.$$set = (u) => {
    o(17, t = q(q({}, t), Y(u))), "svelteInit" in u && o(5, a = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, t = Y(t), [i, l, p, c, s, a, r, n, C, I];
}
class tt extends Ae {
  constructor(t) {
    super(), qe(this, t, et, $e, Ve, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, A = window.ms_globals.tree;
function nt(e, t = {}) {
  function o(i) {
    const l = j(), n = new tt({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? A;
          return a.nodes = [...a.nodes, s], Z({
            createPortal: D,
            node: A
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((x) => x.svelteInstance !== l), Z({
              createPortal: D,
              node: A
            });
          }), s;
        },
        ...i.props
      }
    });
    return l.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = lt(o, i), t;
  }, {}) : {};
}
function lt(e, t) {
  return typeof t == "number" && !rt.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const l = R.Children.toArray(e._reactElement.props.children).map((n) => {
      if (R.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: s
        } = B(n.props.el);
        return R.cloneElement(n, {
          ...n.props,
          el: s,
          children: [...R.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return l.originalChildren = e._reactElement.props.children, t.push(D(R.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: l
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((l) => {
    e.getEventListeners(l).forEach(({
      listener: r,
      type: s,
      useCapture: a
    }) => {
      o.addEventListener(s, r, a);
    });
  });
  const i = Array.from(e.childNodes);
  for (let l = 0; l < i.length; l++) {
    const n = i[l];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: s
      } = B(n);
      t.push(...s), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function it(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const T = ce(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: l
}, n) => {
  const r = ae(), [s, a] = ue([]), {
    forceClone: x
  } = ge(), p = x ? !0 : t;
  return de(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function m() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), it(n, f), o && f.classList.add(...o.split(" ")), i) {
        const h = ot(i);
        Object.keys(h).forEach((_) => {
          f.style[_] = h[_];
        });
      }
    }
    let d = null;
    if (p && window.MutationObserver) {
      let f = function() {
        var I, u, E;
        (I = r.current) != null && I.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: _,
          clonedElement: C
        } = B(e);
        c = C, a(_), c.style.display = "contents", m(), (E = r.current) == null || E.appendChild(c);
      };
      f();
      const h = Oe(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: l
        });
      }, 50);
      d = new window.MutationObserver(h), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", m(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, p, o, i, n, l]), R.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...s);
});
function st(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ct(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !st(e))
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
function S(e, t) {
  return ee(() => ct(e, t), [e, t]);
}
function at(e) {
  return Object.keys(e).reduce((t, o) => (e[o] !== void 0 && (t[o] = e[o]), t), {});
}
function se(e, t, o) {
  const i = e.filter(Boolean);
  if (i.length !== 0)
    return i.map((l, n) => {
      var x;
      if (typeof l != "object")
        return t != null && t.fallback ? t.fallback(l) : l;
      const r = {
        ...l.props,
        key: ((x = l.props) == null ? void 0 : x.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let s = r;
      Object.keys(l.slots).forEach((p) => {
        if (!l.slots[p] || !(l.slots[p] instanceof Element) && !l.slots[p].el)
          return;
        const c = p.split(".");
        c.forEach((_, C) => {
          s[_] || (s[_] = {}), C !== c.length - 1 && (s = r[_]);
        });
        const m = l.slots[p];
        let d, w, f = (t == null ? void 0 : t.clone) ?? !1, h = t == null ? void 0 : t.forceClone;
        m instanceof Element ? d = m : (d = m.el, w = m.callback, f = m.clone ?? f, h = m.forceClone ?? h), h = h ?? !!w, s[c[c.length - 1]] = d ? w ? (..._) => (w(c[c.length - 1], _), /* @__PURE__ */ b.jsx(L, {
          params: _,
          forceClone: h,
          children: /* @__PURE__ */ b.jsx(T, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ b.jsx(L, {
          forceClone: h,
          children: /* @__PURE__ */ b.jsx(T, {
            slot: d,
            clone: f
          })
        }) : s[c[c.length - 1]], s = r;
      });
      const a = (t == null ? void 0 : t.children) || "children";
      return l[a] ? r[a] = se(l[a], t, `${n}`) : t != null && t.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
function $(e, t) {
  return e ? /* @__PURE__ */ b.jsx(T, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function O({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...l) => o ? o.map((n, r) => /* @__PURE__ */ b.jsx(L, {
    params: l,
    forceClone: !0,
    children: $(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ b.jsx(L, {
    params: l,
    forceClone: !0,
    children: $(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const {
  withItemsContextProvider: ut,
  useItems: dt,
  ItemHandler: mt
} = we("antd-tree-select-tree-nodes"), ht = nt(ut(["default", "treeData"], ({
  slots: e,
  filterTreeNode: t,
  getPopupContainer: o,
  dropdownRender: i,
  tagRender: l,
  treeTitleRender: n,
  treeData: r,
  onValueChange: s,
  onChange: a,
  children: x,
  maxTagPlaceholder: p,
  elRef: c,
  setSlotParams: m,
  onLoadData: d,
  ...w
}) => {
  const f = S(t), h = S(o), _ = S(l), C = S(i), I = S(n), {
    items: u
  } = dt(), E = u.treeData.length > 0 ? u.treeData : u.default, g = ee(() => ({
    ...w,
    loadData: d,
    treeData: r || se(E, {
      clone: !0
    }),
    dropdownRender: e.dropdownRender ? O({
      slots: e,
      setSlotParams: m,
      key: "dropdownRender"
    }) : C,
    allowClear: e["allowClear.clearIcon"] ? {
      clearIcon: /* @__PURE__ */ b.jsx(T, {
        slot: e["allowClear.clearIcon"]
      })
    } : w.allowClear,
    suffixIcon: e.suffixIcon ? /* @__PURE__ */ b.jsx(T, {
      slot: e.suffixIcon
    }) : w.suffixIcon,
    prefix: e.prefix ? /* @__PURE__ */ b.jsx(T, {
      slot: e.prefix
    }) : w.prefix,
    switcherIcon: e.switcherIcon ? O({
      slots: e,
      setSlotParams: m,
      key: "switcherIcon"
    }) : w.switcherIcon,
    getPopupContainer: h,
    tagRender: e.tagRender ? O({
      slots: e,
      setSlotParams: m,
      key: "tagRender"
    }) : _,
    treeTitleRender: e.treeTitleRender ? O({
      slots: e,
      setSlotParams: m,
      key: "treeTitleRender"
    }) : I,
    filterTreeNode: f || t,
    maxTagPlaceholder: e.maxTagPlaceholder ? O({
      slots: e,
      setSlotParams: m,
      key: "maxTagPlaceholder"
    }) : p,
    notFoundContent: e.notFoundContent ? /* @__PURE__ */ b.jsx(T, {
      slot: e.notFoundContent
    }) : w.notFoundContent
  }), [C, t, f, h, p, d, w, m, E, e, _, r, I]);
  return /* @__PURE__ */ b.jsxs(b.Fragment, {
    children: [/* @__PURE__ */ b.jsx("div", {
      style: {
        display: "none"
      },
      children: x
    }), /* @__PURE__ */ b.jsx(pe, {
      ...at(g),
      ref: c,
      onChange: (y, ...v) => {
        a == null || a(y, ...v), s(y);
      }
    })]
  });
}));
export {
  ht as TreeSelect,
  ht as default
};
